from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time


def init_driver():
    driver = webdriver.Firefox()
    return driver

def navigate_to_category(driver, url):
    driver.get(url)
    time.sleep(2)

def scroll_to_bottom(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def extract_information(driver, classname):
    elements = driver.find_elements(By.CLASS_NAME, classname)
    info = [element.text for element in elements]
    return info

def extract_image_urls(driver, classname):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, classname)))
        image_elements = driver.find_elements(By.CLASS_NAME, classname)
        image_urls = [element.get_attribute('src') for element in image_elements]
        return image_urls
    except Exception as e:
        print(f"Fehler beim Extrahieren der Bild-URLs: {e}")
        return []


def download_image(image_url, save_path):
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Bild erfolgreich heruntergeladen und gespeichert unter: {save_path}")
        else:
            print(f"Fehler beim Herunterladen des Bildes: HTTP {response.status_code}")
    except Exception as e:
        print(f"Fehler beim Herunterladen des Bildes: {e}")


def download_all_images(driver, classname, download_folder):
    image_urls = extract_image_urls(driver, classname)
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    for idx, image_url in enumerate(image_urls):
        save_path = os.path.join(download_folder, f'image_{idx + 1}.jpg')
        download_image(image_url, save_path)

def main():
    url = 'https://de.aliexpress.com/w/wholesale-Flache-sandalen.html?spm=a2g0o.categorymp.0.0.1912FyQxFyQxUQ&categoryUrlParams=%7B%22q%22%3A%22Flache%20sandalen%22%2C%22s%22%3A%22qp_nw%22%2C%22osf%22%3A%22category_navigate%22%2C%22sg_search_params%22%3A%22%22%2C%22guide_trace%22%3A%22a419bdaa-f1f0-43d9-849b-f06f05004ce9%22%2C%22scene_id%22%3A%2237749%22%2C%22searchBizScene%22%3A%22openSearch%22%2C%22recog_lang%22%3A%22de%22%2C%22bizScene%22%3A%22category_navigate%22%2C%22guideModule%22%3A%22category_navigate_vertical%22%2C%22postCatIds%22%3A%22322%2C201768104%22%2C%22scene%22%3A%22category_navigate%22%7D&isFromCategory=y'
    classname_sold = 'multi--trade--Ktbl2jB'
    classname_name = 'multi--titleText--nXeOvyr'
    classname_image = 'multi--img--1IH3lZb product-img'

    driver = init_driver()
    try:
        navigate_to_category(driver, url)
        scroll_to_bottom(driver)
        sold = extract_information(driver, classname_sold)
        name = extract_information(driver, classname_name)
        print("Extrahierte Verkäufe:", sold)
        print("Extrahierte Namen:", name)
        download_all_images(driver, classname_image, "/Users/dennisschielke/Desktop/Uni/6thSemester/Gründungsmangement/images")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
