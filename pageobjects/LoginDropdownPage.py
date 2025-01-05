from selenium.webdriver.common.by import By

from pageobjects.LoginPageWrapper import LoginPageWrapper


class LoginDropdownPage:
    def __init__(self, driver):
        self.driver = driver

    # Locator for the "Hudl" dropdown option
    hudl_option = (By.XPATH, "//a[@data-qa-id='login-hudl']")

    # Method to click Hudl
    def click_hudl(self):
        hudl_option_element = self.driver.find_element(*self.hudl_option)
        hudl_option_element.click()
        return LoginPageWrapper(self.driver)