from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from PasswordPage import PasswordPage


class LoginPageWrapper:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Locators
    email_input = (By.ID, "username")  # Locator for the email input field
    continue_button = (By.XPATH, "//button[contains(text(), 'Continue')]")  # Locator for the Continue button

    # Method to enter email
    def enterEmail(self, email: str):
        email_element = self.driver.find_element(*self.email_input)
        email_element.clear()  # Clears any pre-filled data before entering
        email_element.send_keys(email)

    # Method to click the "Continue" button
    def clickContinue(self):
        continue_button_element = self.driver.find_element(*self.continue_button)
        continue_button_element.click()

        # When continue is clicked, navigate to the PasswordPage
        return PasswordPage(self.driver)
