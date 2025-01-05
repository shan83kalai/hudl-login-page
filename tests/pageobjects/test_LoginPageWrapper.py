from unittest.mock import MagicMock

import pytest

from pageobjects.LoginPageWrapper import LoginPageWrapper
from pageobjects.PasswordPage import PasswordPage


@pytest.fixture
def mock_driver():
    """Fixture to create a mocked WebDriver instance."""
    driver = MagicMock()
    return driver


@pytest.fixture
def login_page(mock_driver):
    """Fixture to create a LoginPageWrapper instance with a mocked driver."""
    return LoginPageWrapper(driver=mock_driver)


def test_enter_email(login_page, mock_driver):
    """
    Test the `enter_email` method.
    - Verifies that the email input element is located correctly.
    - Ensures the `clear` and `send_keys` methods are called with the correct arguments.
    """
    # Mock the WebDriver's find_element method and the element it returns
    mock_email_element = MagicMock()
    mock_driver.find_element.return_value = mock_email_element

    # Sample email to test
    test_email = "test@example.com"

    # Call the method
    login_page.enter_email(test_email)

    # Assertions
    mock_driver.find_element.assert_called_once_with(*LoginPageWrapper.email_input)
    mock_email_element.clear.assert_called_once()
    mock_email_element.send_keys.assert_called_once_with(test_email)


def test_click_continue_button(login_page, mock_driver):
    """
    Test the `click_continue_button` method.
    - Verifies that the continue button element is located correctly.
    - Ensures the `click` method is called on the button element.
    - Confirms the method returns a `PasswordPage` object.
    """
    # Mock the WebDriver's find_element method and the button element it returns
    mock_continue_button_element = MagicMock()
    mock_driver.find_element.return_value = mock_continue_button_element

    # Call the method
    result = login_page.click_continue_button()

    # Assertions
    mock_driver.find_element.assert_called_once_with(*LoginPageWrapper.continue_button)
    mock_continue_button_element.click.assert_called_once()
    assert isinstance(result, PasswordPage)
