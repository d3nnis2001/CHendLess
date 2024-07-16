from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from gooey import Gooey, GooeyParser
from os import path
from mongosave import store_page, check_duplicates
from utils import get_agent, check_window_size, trim_link
import time
import winsound
import re

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
        print(f"Fehler beim Extrahieren der Bild-URLs: {type(e).__name__}")
    
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

def add_page_to_link(link: str):
    page: str = "&page="
    if not link.endswith(page):
        link += page
    return link

def link(value):
    # Check if link is valid
    link = str(value)
    regex = re.compile(r'^(?:http|ftp)s?://.*')
    
    if not link or not re.match(regex, link) or link == '':
        raise TypeError("The input must be a valid URL.")
    
    return link

@Gooey(show_preview_warning = False,
       program_name = "CHendLess",
       show_success_modal = False,
       show_restart_button = False,
       image_dir = path.dirname(path.abspath(__file__)) + "\images",
       # clear_before_run = True,
       default_size = (650, 580),
       menu = [{
        'name': 'Info',
        'items': [{
                'type': 'Link',
                'menuTitle': 'GitHub Repository',
                'url': 'https://github.com/d3nnis2001/CHendLess'
            }]
        }])
def main():
    parser = GooeyParser(description="Scrape products from an AliExpress category and store them in a MongoDB database.")
    parser.add_argument("Link", action = "store", help = "The category to be scraped", type = link)
    parser.add_argument("--head", action = "store_true", metavar = "Run with head", help = "When executed in head mode, Firefox will launch in the foreground rather than operating in the background.")

    args = parser.parse_args()

    final_url = add_page_to_link(args.Link)
    xpath_cardlistdivs = '//*[@id="card-list"]/div'
    relative_xpath_sold = './div/div/a/div[2]/div[2]/span'
    relative_xpath_name = './div/div/a/div[2]/div[1]'
    relative_xpath_image = './div/div/a/div[1]/img'
    relative_xpath_image_alt = './div/div/a/div[1]/div[1]/div[1]/div/img'
    relative_xpath_price = './div/div/a/div[2]/div[3]/div[1]'
    relative_xpath_price_no_sold = './div/div/a/div[2]/div[2]/div[1]'
    relative_xpath_productlink = './div/div/a'
    xpath_category = '//*[@id="search-words"]'
    print("INIT")

    driver = init_driver(not args.head)
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

            # Unclean way to check if the xpath for the image is working, as it breaks with non-proper categories. TODO: Fix this
            try:
                WebDriverWait(divs[0], 10).until(EC.presence_of_all_elements_located((By.XPATH, relative_xpath_image)))
                image = handle_image(divs[0], relative_xpath_image)
            except Exception as e:
                print("Keine richtige Kategorie. WECHSLE den relativen Pfad!")
                relative_xpath_image = relative_xpath_image_alt

            for i, div in enumerate(divs, start=1):
                entries.append(handle_card(card = div, relative_xpath_sold = relative_xpath_sold, relative_xpath_price_no_sold = relative_xpath_price_no_sold, relative_xpath_name = relative_xpath_name, relative_xpath_price = relative_xpath_price, relative_xpath_image = relative_xpath_image, relative_xpath_productlink = relative_xpath_productlink))
                # print(f'Div {i}: ', entries[i-1])
            store_page(entries=entries, category_name=category)
            page_num += 1
        check_duplicates(category_name=category)
    finally:
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        driver.quit()

if __name__ == "__main__":
    main()