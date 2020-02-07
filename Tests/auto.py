from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('/Users/denia.dobras/PycharmProjects/SeleniumFeb2020/venv/bin/chromedriver')
class PageLocators:
    name = (By.NAME, 'q')
    search_button = (By.XPATH,"//div[@class='FPdoLc tfB0Bf']//input[@name='btnK']")

driver.get('https://www.google.com/')
driver.find_element(*PageLocators.name).send_keys("Software testing")
driver.find_element(*PageLocators.search_button).click()
driver.quit()