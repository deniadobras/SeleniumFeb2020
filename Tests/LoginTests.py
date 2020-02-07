from Pages.HomePage import HomePage, HomePageLocators
from Pages.LoginPage import LoginPage
from Utils.TestBase import setup_browser, close_browser

username = "deniad"
password = "Test1234"

expected_text = "Welcome, deniad."

driver = setup_browser()
login_page = LoginPage(driver, navigate=True)
login_page.loginWithCorrectCredentials(username, password)
home_page = HomePage(driver)
actual_text = home_page.getWelcomeMessage(HomePageLocators.welcome_elem)
assert actual_text == expected_text
close_browser(driver)




