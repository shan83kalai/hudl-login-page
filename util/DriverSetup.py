from selenium import webdriver


class DriverSetup:
    @staticmethod
    def get_driver():
        # Use Chrome as the default driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver
