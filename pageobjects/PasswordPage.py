from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pageobjects.HudlHomePage import HudlHomePage


class PasswordPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Locators
    password_input = (By.ID, "password")  # Locator for the password input field
    continue_button = (By.XPATH, "//button[contains(text(), 'Continue')]")  # Locator for the Continue button
    # Locator for the error message
    error_message_locator = (By.ID, "error-element-password")

    # Method to enter the password
    def enter_password(self, password: str):
        password_element = self.driver.find_element(*self.password_input)
        password_element.clear()  # Clears any pre-filled data before entering
        password_element.send_keys(password)

    # Method to click the "Continue" button
    def click_continue(self):
        continue_button_element = self.driver.find_element(*self.continue_button)
        continue_button_element.click()

        # Check if error message exists
        try:
            self.driver.find_element(*self.error_message_locator)
            return self  # Stay on LoginPageWrapper
        except Exception:
            return HudlHomePage(self.driver)  # Navigate to PasswordPage if no error

        # Method to get the error message

    def get_error_message(self) -> str | None:
        try:
            error_element = self.driver.find_element(*self.error_message_locator)
            return error_element.text  # Extract the error message
        except Exception:
            return None  # Return None if no error message is present

