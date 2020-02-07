from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://bento3-qa.pbs.org/admin/")
username = driver.find_element_by_id("id_username")
username.send_keys("deniad")
password = driver.find_element_by_id("id_password")
password.send_keys("Test1234")
submit = driver.find_element_by_css_selector("[value='Log in']")
submit.click()
welcome_elem = driver.find_element_by_class_name("user-info")
welcome_text = welcome_elem.text.replace('\n', ' ')
expected_text = "Welcome, deniad."


assert expected_text == welcome_text

driver.close()