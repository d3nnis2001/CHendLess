from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from mongosave import store_page, check_duplicates
from utils import get_agent, check_window_size, trim_link
import time

sleep = 2

def init_driver(headless: bool):
    options = webdriver.FirefoxOptions()
    if headless: options.add_argument("--headless")
    options.add_argument(f"--user-agent={get_agent()}")
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(4096, 3072) # Use increased window size to save more products
    return driver

def navigate_to_category(driver, url):
    driver.get(url)
    # Check for captcha, return if so. ADD captcha solver
    if len(driver.find_elements(By.XPATH, '//*[@id="baxia-punish"]')) == 1:
        print("ERROR: Loading page stopped by captcha: Returning!")
        return False
    
    # The possibility exists that a +18 accept button appears, this will click it.
    if len(driver.find_elements(By.XPATH, '/html/body/div[7]/div[2]/div/div[2]')) == 1:
        print("ERROR: Loading page stopped by 18+ confirmation... Attempting to click!") 
        driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div[2]/div/div[2]/div').click()
        time.sleep(1)
        print("CLICKED the link! Continue...now!")

    time.sleep(sleep)
    print("ENTERED page!")
    return True

# This is still necessary, do not remove
def scroll_to_bottom(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def handle_card(card, relative_xpath_sold, relative_xpath_name, relative_xpath_price, relative_xpath_price_no_sold, relative_xpath_image, relative_xpath_productlink):
    entry = []
    try:
        sold = card.find_element(By.XPATH, relative_xpath_sold).get_attribute('innerHTML')
    except NoSuchElementException as e:
        sold = None

    name = card.find_element(By.XPATH, relative_xpath_name).get_attribute('innerText')
    link = card.find_element(By.XPATH, relative_xpath_productlink).get_attribute('href')
    price = handle_price(card, relative_xpath_price) if sold else handle_price(card, relative_xpath_price_no_sold)

    image = None
    try:
        WebDriverWait(card, 10).until(EC.presence_of_all_elements_located((By.XPATH, relative_xpath_image)))
        image = handle_image(card, relative_xpath_image)
    except Exception as e:
        print(f"Fehler beim Extrahieren der Bild-URLs: {type(e).__name__}, {e}")
    
    # Save in the order that it's saved in the DB
    entry.append(name)
    entry.append(price)
    entry.append(sold)
    entry.append(image)
    entry.append(trim_link(link))
    return entry

def handle_price(card, relative_xpath_price):
    elements = card.find_elements(By.XPATH, relative_xpath_price)
    if(len(elements)) == 0:
        return None
    else:
        prices = []
        price = ''.join([span.text for span in elements])
        prices.append(price)
        return prices[0]
    
def handle_image(card, relative_xpath_image):
        image_elements = card.find_elements(By.XPATH, relative_xpath_image)
        image_urls = image_elements[0].get_attribute('src')
        return image_urls

def extract_category(driver: webdriver, xpath: str):
    elements = driver.find_elements(By.XPATH, xpath)
    return elements[0].get_attribute('value')

def main():
    final_url = 'https://de.aliexpress.com/w/wholesale-Spritzpistole.html?spm=a2g0o.home.allcategoriespc.25.3c5812e29wzpW5&categoryUrlParams=%7B%22q%22%3A%22Spritzpistole%22%2C%22s%22%3A%22qp_nw%22%2C%22osf%22%3A%22categoryNagivateOld%22%2C%22sg_search_params%22%3A%22%22%2C%22guide_trace%22%3A%22b73e96d1-cbaa-4530-9f16-50e0569311e7%22%2C%22scene_id%22%3A%2230630%22%2C%22searchBizScene%22%3A%22openSearch%22%2C%22recog_lang%22%3A%22de%22%2C%22bizScene%22%3A%22categoryNagivateOld%22%2C%22guideModule%22%3A%22unknown%22%2C%22postCatIds%22%3A%221420%22%2C%22scene%22%3A%22category_navigate%22%7D&isFromCategory=y'
    xpath_cardlistdivs = '//*[@id="card-list"]/div'
    relative_xpath_sold = './div/div/a/div[2]/div[2]/span'
    relative_xpath_name = './div/div/a/div[2]/div[1]'
    relative_xpath_image = './div/div/a/div[1]/img'
    relative_xpath_price = './div/div/a/div[2]/div[3]/div[1]'
    relative_xpath_price_no_sold = './div/div/a/div[2]/div[2]/div[1]'
    relative_xpath_productlink = './div/div/a'
    xpath_category = '//*[@id="search-words"]'
    print("INIT")

    driver = init_driver(True)
    check_window_size(driver=driver)

    try:
        page_num = 1
        category = 'cat'
        while True:
            url = final_url + str(page_num)
            hasEntered = navigate_to_category(driver, url)
            if not hasEntered: return
            print("Current page: ", url)
            scroll_to_bottom(driver)
            category = extract_category(driver=driver, xpath=xpath_category)
            entries = []
            divs = driver.find_elements(By.XPATH, xpath_cardlistdivs)
            if len(divs) == 0:
                print("INFO: No elements found, last page")
                break
            for i, div in enumerate(divs, start=1):
                entries.append(handle_card(card = div, relative_xpath_sold = relative_xpath_sold, relative_xpath_price_no_sold = relative_xpath_price_no_sold, relative_xpath_name = relative_xpath_name, relative_xpath_price = relative_xpath_price, relative_xpath_image = relative_xpath_image, relative_xpath_productlink = relative_xpath_productlink))
                # print(f'Div {i}: ', entries[i-1])
            store_page(entries=entries, category_name=category)
            page_num += 1
        check_duplicates(category_name=category)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()