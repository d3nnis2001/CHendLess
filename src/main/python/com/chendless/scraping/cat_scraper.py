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

def scroll_to_bottom(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def extract_information(driver: webdriver, classname: str):
    elements = driver.find_elements(By.CLASS_NAME, classname)
    info = [element.text for element in elements]
    return info

# Use a specific function to add spans together
def extract_price(driver: webdriver, xpath_price: str):
    elements = driver.find_elements(By.XPATH, xpath_price)
    prices = []
    for element in elements:
        spans = element.find_elements(By.XPATH, './span')
        price = ''.join([span.text for span in spans])
        prices.append(price)
    return prices

def extract_image_urls(driver, xpath):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        image_elements = driver.find_elements(By.XPATH, xpath)
        image_urls = [element.get_attribute('src') for element in image_elements]
        return image_urls
    except Exception as e:
        print(f"Fehler beim Extrahieren der Bild-URLs: {type(e).__name__}, {e}")
        return []

def main():
    url = 'https://de.aliexpress.com/w/wholesale-Flache-sandalen.html?spm=a2g0o.categorymp.0.0.1912FyQxFyQxUQ&categoryUrlParams=%7B%22q%22%3A%22Flache%20sandalen%22%2C%22s%22%3A%22qp_nw%22%2C%22osf%22%3A%22category_navigate%22%2C%22sg_search_params%22%3A%22%22%2C%22guide_trace%22%3A%22a419bdaa-f1f0-43d9-849b-f06f05004ce9%22%2C%22scene_id%22%3A%2237749%22%2C%22searchBizScene%22%3A%22openSearch%22%2C%22recog_lang%22%3A%22de%22%2C%22bizScene%22%3A%22category_navigate%22%2C%22guideModule%22%3A%22category_navigate_vertical%22%2C%22postCatIds%22%3A%22322%2C201768104%22%2C%22scene%22%3A%22category_navigate%22%7D&isFromCategory=y'
    classname_sold = 'multi--trade--Ktbl2jB'
    classname_name = 'multi--titleText--nXeOvyr'
    # classname_image = 'multi--img--1IH3lZb product-img'
    xpath_image = '//*[@id="card-list"]//div/a/div[1]/img'
    xpath_price = '//*[@id="card-list"]/div/div/div/a/div[2]/div[3]/div[1]'
    print("INIT")

    driver = init_driver(True)
    try:
        navigate_to_category(driver, url)
        # scroll_to_bottom(driver)
        sold = extract_information(driver, classname_sold)
        name = extract_information(driver, classname_name)
        price = extract_price(driver, xpath_price)
        print("Extrahierte Verkäufe:", sold)
        print("Extrahierte Namen:", name)
        print("Extrahierte Preise: ", price)
        image_urls = extract_image_urls(driver, xpath_image)

        if not (len(image_urls) == len(sold) == len(name) == len(price)):
            print("!! Size of stored data is NOT equal !!\nCheck if the window size is correct!")
            return
        store_page(sold=sold, name=name, price=price, image_urls=image_urls)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main()