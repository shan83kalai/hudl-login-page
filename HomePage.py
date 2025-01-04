from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from LoginDropdownPage import DropdownPage


class HomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Locator for the 'Login' button (top right corner)
    login_button = (By.XPATH, "//a[contains(@class, 'mainnav__item') and contains(@data-qa-id, 'login-select')]")

    # Method to click the 'Login' button
    def clickLoginButton(self):
        login_button_element = self.driver.find_element(*self.login_button)
        login_button_element.click()
        return DropdownPage(self.driver)  # Ensure DropdownPage is returned