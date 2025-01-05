from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class HudlHomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Locator
    display_name = (By.CLASS_NAME, "hui-globaluseritem__display-name")  # Locator for the display name element

    # Method to get the display name
    def get_display_user_name(self) -> str:
        display_element = self.driver.find_element(*self.display_name)
        return display_element.text