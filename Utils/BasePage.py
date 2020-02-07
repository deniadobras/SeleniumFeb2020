from selenium.webdriver.chrome.webdriver import  WebDriver
from selenium.webdriver.support.select import Select

from Utils.TestBase import setup_browser


class BaseLocators:
    pass

class BasePage:
    PAGE = ""

    def __init__(self, driver: WebDriver, navigate=False):
        self.driver = driver
        if not driver:
            driver = setup_browser()
        if navigate:
            driver.get(self.PAGE)

