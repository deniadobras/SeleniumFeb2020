from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Utils.BasePage import BasePage


class HomePageLocators:
    welcome_elem = (By.CLASS_NAME, "user-info")


class HomePage(BasePage):

    def getWelcomeMessage(self, welcometext):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(welcometext))
        welcome_element_text = self.driver.find_element(*welcometext)
        return welcome_element_text.text.replace("\n", " ")
