from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HudlHomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Locator for the display name element
    display_name = (By.CLASS_NAME, "fanWebnav_displayName__gvbGS")

    def get_display_user_name(self):
        """Fetch the user's display name after waiting for its presence."""
        # Wait until the element is present and visible
        display_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.display_name)  # Wait for the element to be present in the DOM
        )
        return display_element.text.strip()