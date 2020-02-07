from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Utils.BasePage import BasePage


class LoginPageLocators:
    username = (By.ID, "id_username")
    password = (By.ID, "id_password")
    submit = (By.XPATH, "//div[@class='submit-row']//input")
    welcome_elem = (By.CLASS_NAME, "user-info")



class LoginPage(BasePage):
    PAGE = "https://bento3-qa.pbs.org/admin/"

    def __init__(self, driver, navigate):
        super().__init__(driver, navigate)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.username))


    def loginWithCorrectCredentials(self, username, password):
        self.driver.find_element(*LoginPageLocators.username).send_keys(username)
        self.driver.find_element(*LoginPageLocators.password).send_keys(password)
        self.driver.find_element(*LoginPageLocators.submit).click()



