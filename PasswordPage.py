from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from HudlHomePage import HudlHomePage  # Importing HudlHomePage class


class PasswordPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Locators
    password_input = (By.ID, "password")  # Locator for the password input field
    continue_button = (By.XPATH, "//button[contains(text(), 'Continue')]")  # Locator for the Continue button

    # Method to enter the password
    def enterPassword(self, password: str):
        password_element = self.driver.find_element(*self.password_input)
        password_element.clear()  # Clears any pre-filled data before entering
        password_element.send_keys(password)

    # Method to click the "Continue" button
    def clickContinue(self):
        continue_button_element = self.driver.find_element(*self.continue_button)
        continue_button_element.click()

        # Return the new page object HudlHomePage
        return HudlHomePage(self.driver)
