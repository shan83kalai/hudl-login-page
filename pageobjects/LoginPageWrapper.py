from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pageobjects.PasswordPage import PasswordPage
from util.ValidationUtils import get_validation_message


class LoginPageWrapper:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Locators
    email_input = (By.ID, "username")  # Locator for the email input field
    continue_button = (By.XPATH, "//button[contains(text(), 'Continue')]")  # Locator for the Continue button
    email_error_message = (By.ID, "error-element-username")  # Locator for email validation error message

    # Method to enter email
    def enter_email(self, email: str):
        email_element = self.driver.find_element(*self.email_input)
        email_element.clear()  # Clears any pre-filled data before entering
        email_element.send_keys(email)

    def click_continue_button(self):
        """
        Clicks the 'Continue' button and navigates to the PasswordPage if no error is present.
        If an error is shown, stays on the current page and returns self.
        """
        continue_button_element = self.driver.find_element(*self.continue_button)
        continue_button_element.click()

        try:
            # Check if the error message is displayed
            error_element = self.driver.find_element(*self.email_error_message)
            if error_element.is_displayed():
                # Stay on current page if error exists
                return self
        except Exception:
            # If no error element exists, assume navigation occurs
            pass

        # Navigate to PasswordPage if no errors
        return PasswordPage(self.driver)

    # Use the utility to get the validation message
    def get_validation_message(self, field_locator: tuple) -> str:
        return get_validation_message(self.driver, field_locator)

    # Method to retrieve the input error message
    def get_input_error_message(self) -> str:
        """
        Fetches the error message displayed for invalid input in the email field.

        Returns:
            str: The error message text, or an empty string if no error message is displayed.
        """
        try:
            error_element = self.driver.find_element(*self.email_error_message)
            if error_element.is_displayed():
                return error_element.text.strip()
        except Exception:
            # If no error element is present, return an empty string
            return ""
        return ""

