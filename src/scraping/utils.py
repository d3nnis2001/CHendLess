from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from selenium import webdriver

def get_agent():
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   

    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

    # Get Random User Agent String.
    user_agent = user_agent_rotator.get_random_user_agent()
    return user_agent

def check_window_size(driver: webdriver):
    size = driver.get_window_size()
    print('Selenium webdriver size is: ', size)
    if size['width'] != 4096 and size['height'] != 3072:
        print('Selenium webdriver size is NOT 4k! This will result in an image timeout!')