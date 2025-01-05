from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pageobjects.PasswordPage import PasswordPage


class LoginPageWrapper:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Locators
    email_input = (By.ID, "username")  # Locator for the email input field
    continue_button = (By.XPATH, "//button[contains(text(), 'Continue')]")  # Locator for the Continue button
    # Locator for the error message
    error_message_locator = (By.ID, "error-element-password")

    # Method to enter email
    def enter_email(self, email: str):
        email_element = self.driver.find_element(*self.email_input)
        email_element.clear()  # Clears any pre-filled data before entering
        email_element.send_keys(email)

    # Method to click the "Continue" button
    def click_continue_button(self):
        continue_button_element = self.driver.find_element(*self.continue_button)
        continue_button_element.click()

        # Check if error message exists
        try:
            self.driver.find_element(*self.error_message_locator)
            return self  # Stay on LoginPageWrapper
        except Exception:
            return PasswordPage(self.driver)  # Navigate to PasswordPage if no error

    # Method to get the error message
    def get_error_message(self) -> str | None:
        try:
            error_element = self.driver.find_element(*self.error_message_locator)
            return error_element.text  # Extract the error message
        except Exception:
            return None  # Return None if no error message is present
