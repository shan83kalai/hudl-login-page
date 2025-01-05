from pageobjects.HomePage import HomePage
from project_logging.CustomLogger import logger
from util.ConfigReader import ConfigReader
from util.DriverSetup import DriverSetup


def navigate_to_hudl_login(driver, config):
    """Navigate to Hudl login by reading configuration and clicking login steps."""
    base_url = config["DEFAULT"]["BASE_URL"]
    logger.info(f"Navigating to {base_url}")
    driver.get(base_url)
    home_page = HomePage(driver)
    dropdown_page = home_page.click_login_button()
    return dropdown_page.click_hudl()


def proceed_with_email(login_page, user_email):
    """Enter email and proceed to the password page."""
    logger.info(f"Entering email: {user_email}")
    login_page.enter_email(user_email)
    return login_page.click_continue_button()


def test_login():
    driver = DriverSetup.get_driver()
    config = ConfigReader.get_config()

    try:
        login_page = navigate_to_hudl_login(driver, config)
        user_email = config["DEFAULT"]["USER_EMAIL"]
        password = ConfigReader.get_password(config)

        # Proceed with email and password steps
        password_page = proceed_with_email(login_page, user_email)
        logger.info("Entering password and continuing...")
        password_page.enter_password(password)
        hudl_home_page = password_page.click_continue()

        # Validate display name
        display_name = hudl_home_page.get_display_user_name()
        expected_display_name = "Guljar H"
        assert display_name == expected_display_name, (f"Expected display name to be '{expected_display_name}', "
                                                       f"but got '{display_name}'")
        logger.info("Display name verification passed.")
    except Exception as e:
        logger.error(f"An error occurred during the test: {e}", exc_info=True)
        raise
    finally:
        driver.quit()
        logger.info("Browser session closed")


def test_login_wrong_password():
    driver = DriverSetup.get_driver()
    config = ConfigReader.get_config()

    try:
        login_page = navigate_to_hudl_login(driver, config)
        user_email = config["DEFAULT"]["USER_EMAIL"]
        wrong_password = "wrong_password123"

        # Proceed with email and enter wrong password
        password_page = proceed_with_email(login_page, user_email)
        logger.info("Entering wrong password and attempting to log in...")
        password_page.enter_password(wrong_password)
        password_page.click_continue()

        # Verify error message
        error_message = password_page.get_error_message()
        expected_error_message = "Your email or password is incorrect. Try again."
        assert error_message == expected_error_message, (f"Expected error message to be '{expected_error_message}', "
                                                         f"but got '{error_message}'")
        logger.info("Error message verification passed for incorrect password.")
    except Exception as e:
        logger.error(f"An error occurred during the test: {e}", exc_info=True)
        raise
    finally:
        driver.quit()
        logger.info("Browser session closed")


def test_login_empty_password():
    driver = DriverSetup.get_driver()
    config = ConfigReader.get_config()

    try:
        login_page = navigate_to_hudl_login(driver, config)
        user_email = config["DEFAULT"]["USER_EMAIL"]
        empty_password = ""

        # Proceed with email and leave password field empty
        password_page = proceed_with_email(login_page, user_email)
        logger.info("Leaving password field empty...")
        password_page.enter_password(empty_password)

        # Verify validation message
        logger.info("Attempting to continue with an empty password...")
        validation_message = password_page.get_validation_message(password_page.password_input)
        expected_validation_message = "Please fill in this field."
        assert validation_message == expected_validation_message, (f"Expected validation message to be "
                                                                   f"'{expected_validation_message}', "
                                                                   f"but got '{validation_message}'")
        logger.info("Validation message verification passed for empty password.")
    except Exception as e:
        logger.error(f"An error occurred during the test: {e}", exc_info=True)
        raise
    finally:
        driver.quit()
        logger.info("Browser session closed")

def test_login_empty_email():
    driver = DriverSetup.get_driver()
    config = ConfigReader.get_config()

    try:
        # Navigate to the Hudl login page
        login_page = navigate_to_hudl_login(driver, config)
        empty_email = ""  # Empty email field

        # Attempt to proceed with an empty email field
        logger.info("Leaving email field empty...")
        login_page.enter_email(empty_email)

        logger.info("Attempting to continue with an empty email field...")
        validation_message = login_page.get_validation_message(login_page.email_input)

        # Expected validation message
        expected_validation_message = "Please fill in this field."  # Adjust based on browser's behavior
        assert validation_message == expected_validation_message, (f"Expected validation message to be "
                                                                   f"'{expected_validation_message}', "
                                                                   f"but got '{validation_message}'")
        logger.info("Validation message verification passed for empty email field.")
    except Exception as e:
        logger.error(f"An error occurred during test: {e}", exc_info=True)
        raise
    finally:
        driver.quit()
        logger.info("Browser session closed")
