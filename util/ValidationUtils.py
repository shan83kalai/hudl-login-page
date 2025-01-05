from selenium.webdriver.remote.webdriver import WebDriver


def get_validation_message(driver: WebDriver, field_locator: tuple) -> str:
    """
    Fetches the browser's built-in validation message for the given field locator.

    Args:
        driver (WebDriver): Selenium WebDriver instance.
        field_locator (tuple): Locator tuple for the field (e.g., (By.ID, "username")).

    Returns:
        str: The browser's validation message for the specified field.
    """
    try:
        field_element = driver.find_element(*field_locator)
        return driver.execute_script("return arguments[0].validationMessage;", field_element)
    except Exception as e:
        raise RuntimeError(f"Failed to get validation message for {field_locator}: {e}")
