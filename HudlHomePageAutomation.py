import configparser
import os

from cryptography.fernet import Fernet
from selenium import webdriver

from HomePage import HomePage
from LoginPageWrapper import LoginPageWrapper
from project_logging.CustomLogger import logger

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
logger.info(f"Base URL: {base_url}")
user_email = config.get("DEFAULT", "USER_EMAIL")

# Encryption/Decryption Key (set in environment variables for security)
SECRET_KEY = config.get("DEFAULT", "SECRET_KEY")  # Must be stored securely
fernet = Fernet(SECRET_KEY)

# Decrypt the password
encrypted_password = config.get("DEFAULT", "ENCRYPTED_PASSWORD")
password = fernet.decrypt(encrypted_password.encode()).decode()
logger.debug(f"Decrypted Password: {password}")  # Only log in DEBUG level for security

plain_password = config.get("DEFAULT", "PASSWORD")

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the Hudl home page using the BASE_URL from the config file
    logger.info(f"Navigating to {base_url}")
    driver.get(base_url)

    # Step 1: Click the login button and get the dropdown page
    home_page = HomePage(driver)
    dropdown_page = home_page.click_login_button()

    # Step 2: Click the "Hudl" option in the dropdown
    login_page = dropdown_page.click_hudl()

    # Step 3: Enter email and proceed using USER_EMAIL from the config file
    login_page.enter_email(user_email)
    logger.info(f"Entering email: {user_email}")
    password_page = login_page.click_continue_button()

    # Step 4: Enter password and continue
    logger.info("Entering password and continuing...")
    password_page.enter_password(password)
    # password_page.enterPassword(plain_password)
    hudl_home_page = password_page.click_continue()

    # Retrieve and log the display name
    display_name = hudl_home_page.get_display_user_name()
    logger.info(f"Display Name: {display_name}")

    logger.info("Logged in successfully!")

except Exception as e:
    logger.error(f"An error occurred: {e}", exc_info=True)

finally:
    # Close the browser session
    logger.info("Closing the browser.")
    driver.quit()
