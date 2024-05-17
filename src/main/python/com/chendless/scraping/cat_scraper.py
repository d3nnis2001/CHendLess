from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.request import Request, urlopen
from PIL import Image
from mongosave import store_page
import os
import time

def init_driver(headless: bool):
    options = webdriver.FirefoxOptions()
    if headless: options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(4096, 3072) # Use increased window size to save more products
    return driver

def navigate_to_category(driver, url):
    driver.get(url)
    time.sleep(2)
    print("ENTERED page!")

# This is still necessary, do not remove
def scroll_to_bottom(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def append_if_exist(arr, entry, attr):
    if arr:
        entry.append(getattr(arr[0], attr))
    else:
        entry.append(None)

def handle_card(card, relative_xpath_sold, relative_xpath_name, relative_xpath_price, relative_xpath_image):
    entry = []
    sold = card.find_elements(By.XPATH, relative_xpath_sold)
    name = card.find_elements(By.XPATH, relative_xpath_name)
    price = handle_price(card, relative_xpath_price)
    image = None
    try:
        WebDriverWait(card, 10).until(EC.presence_of_all_elements_located((By.XPATH, relative_xpath_image)))
        image = handle_image(card, relative_xpath_image)
    except Exception as e:
        print(f"Fehler beim Extrahieren der Bild-URLs: {type(e).__name__}, {e}")
    append_if_exist(sold, entry, 'text')
    append_if_exist(name, entry, 'text')
    entry.append(price)
    entry.append(image)
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
    url = 'https://de.aliexpress.com/w/wholesale-Fensterfolien-und-Sonnenschutz.html?spm=a2g0o.home.allcategoriespc.31.44e312e2NkNsid&categoryUrlParams=%7B"q"%3A"Fensterfolien%20und%20Sonnenschutz"%2C"s"%3A"qp_nw"%2C"osf"%3A"categoryNagivateOld"%2C"sg_search_params"%3A""%2C"guide_trace"%3A"e39589b9-3b85-4535-8cf6-fe88d3deb2d0"%2C"scene_id"%3A"30630"%2C"searchBizScene"%3A"openSearch"%2C"recog_lang"%3A"de"%2C"bizScene"%3A"categoryNagivateOld"%2C"guideModule"%3A"unknown"%2C"postCatIds"%3A"34%2C201355758"%2C"scene"%3A"category_navigate"%7D&isFromCategory=y'
    xpath_cardlistdivs = '//*[@id="card-list"]/div'
    relative_xpath_sold = './div/div/a/div[2]/div[2]/span'
    relative_xpath_name = './div/div/a/div[2]/div[1]'
    relative_xpath_image = './div/div/a/div[1]/img'
    relative_xpath_price = './div/div/a/div[2]/div[3]/div[1]/span'
    xpath_category = '//*[@id="search-words"]'
    print("INIT")

    driver = init_driver(True)

    try:
        navigate_to_category(driver, url)
        scroll_to_bottom(driver)
        category = extract_category(driver=driver, xpath=xpath_category)
        entries = []
        divs = driver.find_elements(By.XPATH, xpath_cardlistdivs)
        for i, div in enumerate(divs, start=1):
            entries.append(handle_card(card = div, relative_xpath_sold = relative_xpath_sold, relative_xpath_name = relative_xpath_name, relative_xpath_price = relative_xpath_price, relative_xpath_image = relative_xpath_image))
            print(f'Div {i}: ', entries[i-1])
        store_page(entries=entries, category_name=category)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()