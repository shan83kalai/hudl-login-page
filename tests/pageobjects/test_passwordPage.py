from unittest.mock import MagicMock

import pytest

from pageobjects.HudlHomePage import HudlHomePage
from pageobjects.PasswordPage import PasswordPage


@pytest.fixture
def mock_driver():
    """Fixture to create a mocked WebDriver instance."""
    driver = MagicMock()
    return driver


@pytest.fixture
def password_page(mock_driver):
    """Fixture to create a PasswordPage instance with a mocked driver."""
    return PasswordPage(driver=mock_driver)


def test_enter_password(password_page, mock_driver):
    """
    Test the `enter_password` method.
    - Verifies that the correct password input element is located.
    - Ensures the `clear` and `send_keys` methods are called with the correct arguments.
    """
    # Mock the WebDriver's find_element method and input element
    mock_password_element = MagicMock()
    mock_driver.find_element.return_value = mock_password_element

    # Call the enter_password method
    test_password = "TestPassword123"
    password_page.enter_password(test_password)

    # Assertions
    mock_driver.find_element.assert_called_once_with(*PasswordPage.password_input)
    mock_password_element.clear.assert_called_once()
    mock_password_element.send_keys.assert_called_once_with(test_password)


def test_click_continue(password_page, mock_driver):
    """
    Test the `click_continue` method.
    - Verifies that the "Continue" button is located.
    - Ensures the `click` method is called on the button element.
    - Checks if a `HudlHomePage` object is returned.
    """
    # Mock the WebDriver's find_element method and button element
    mock_continue_button_element = MagicMock()
    mock_driver.find_element.return_value = mock_continue_button_element

    # Call the click_continue method and capture the returned value
    result = password_page.click_continue()

    # Assertions
    mock_driver.find_element.assert_called_once_with(*PasswordPage.continue_button)
    mock_continue_button_element.click.assert_called_once()
    assert isinstance(result, HudlHomePage)