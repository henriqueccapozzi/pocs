from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
import time


def set_chrome_options() -> None:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options


def get_element_text(driver: webdriver.Chrome) -> None:
    URL = "https://the-faster.herokuapp.com/login"
    driver.get(URL)
    elements = driver.find_elements_by_tag_name("input")
    for element in elements:
        print(element.get_property("name"))
        print("*" * 60)
        # print(dir(element))


if __name__ == "__main__":
    driver = webdriver.Chrome(options=set_chrome_options())
    # Do stuff with your driver
    get_element_text(driver)
    driver.close()
