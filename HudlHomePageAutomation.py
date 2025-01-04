from selenium import webdriver
from HomePage import HomePage
from LoginPageWrapper import LoginPageWrapper
import os
import configparser

# Read config file using the current script's location
config = configparser.ConfigParser()

# Dynamically get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to Constants.properties
config_file_path = os.path.join(current_dir, "Constants.properties")

# Read the config file
config.read(config_file_path)

# Example usage: Fetch BASE_URL from the config
base_url = config.get("DEFAULT", "BASE_URL")
print(f"Base URL: {base_url}")
user_email = config.get("DEFAULT", "USER_EMAIL")

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the Hudl home page using the BASE_URL from the config file
    driver.get(base_url)

    # Step 1: Click the login button and get the dropdown page
    home_page = HomePage(driver)
    dropdown_page = home_page.clickLoginButton()

    # Step 2: Click the "Hudl" option in the dropdown
    dropdown_page.clickHudl()

    # Step 3: Enter email and proceed using USER_EMAIL from the config file
    login_page = LoginPageWrapper(driver)
    login_page.enterEmail(user_email)
    login_page.clickContinue()

    print("Logged in successfully!")

finally:
    # Close the browser session
    driver.quit()
