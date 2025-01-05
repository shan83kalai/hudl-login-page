from pageobjects.HomePage import HomePage
from project_logging.CustomLogger import logger
from util.ConfigReader import ConfigReader
from util.DriverSetup import DriverSetup


def test_login():
    # Initialize WebDriver
    driver = DriverSetup.get_driver()
    config = ConfigReader.get_config()
    try:

        # Read base URL and credentials from config
        base_url = config["DEFAULT"]["BASE_URL"]
        user_email = config["DEFAULT"]["USER_EMAIL"]
        password = ConfigReader.get_password(config)

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
        logger.info(f"Retrieved Display Name: {display_name}")

        # Verify the expected display name
        expected_display_name = "Guljar H"
        assert display_name == expected_display_name, (f"Expected display name to be '{expected_display_name}', "
                                                       f"but got '{display_name}'")
        logger.info("Display name verification passed.")


    except Exception as e:
        logger.error(f"An error occurred during the test: {e}", exc_info=True)
        raise  # Re-raise the exception to ensure the test fails

    finally:
        # Quit the browser
        driver.quit()
        logger.info("Browser session closed")

def test_login_wrong_password():
    # Initialize WebDriver
    driver = DriverSetup.get_driver()
    config = ConfigReader.get_config()
    try:
        # Read base URL and credentials from config
        base_url = config["DEFAULT"]["BASE_URL"]
        user_email = config["DEFAULT"]["USER_EMAIL"]
        wrong_password = "wrong_password123"  # Deliberate incorrect password

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

        # Step 4: Enter the wrong password
        logger.info("Entering wrong password and attempting to log in...")
        password_page.enter_password(wrong_password)
        password_page.click_continue()

        # Step 5: Verify error message for incorrect password
        error_message = password_page.get_error_message()
        logger.info(f"Error Message: {error_message}")

        # Update expected error message to match the actual application behavior
        expected_error_message = "Your email or password is incorrect. Try again."
        assert error_message == expected_error_message, (f"Expected error message to be '{expected_error_message}', "
                                                         f"but got '{error_message}'")
        logger.info("Error message verification passed for incorrect password.")

    except Exception as e:
        logger.error(f"An error occurred during the test: {e}", exc_info=True)
        raise  # Re-raise the exception to ensure the test fails

    finally:
        # Quit the browser
        driver.quit()
        logger.info("Browser session closed")


def test_login_empty_password():
    # Initialize WebDriver
    driver = DriverSetup.get_driver()
    config = ConfigReader.get_config()
    try:
        # Read base URL and credentials from config
        base_url = config["DEFAULT"]["BASE_URL"]
        user_email = config["DEFAULT"]["USER_EMAIL"]
        empty_password = ""  # Empty password

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

        # Step 4: Leave the password field empty
        logger.info("Leaving password field empty...")
        password_page.enter_password(empty_password)  # Simulate leaving the password field empty

        # Step 5: Try clicking the "Continue" button
        logger.info("Attempting to continue with an empty password...")
        validation_message = password_page.get_validation_message(password_page.password_input)

        # Verify the popup message for empty password
        expected_popup_message = "Please fill in this field."  # Adjust if the browser's message differs
        assert validation_message == expected_popup_message, (f"Expected validation message to be '{expected_popup_message}', "
                                                              f"but got '{validation_message}'")
        logger.info("Validation message verification passed for empty password.")

    except Exception as e:
        logger.error(f"An error occurred during the test: {e}", exc_info=True)
        raise  # Re-raise the exception to ensure the test fails

    finally:
        # Quit the browser
        driver.quit()
        logger.info("Browser session closed")