from unittest.mock import MagicMock

import pytest

from pageobjects.LoginDropdownPage import LoginDropdownPage
from pageobjects.LoginPageWrapper import LoginPageWrapper


@pytest.fixture
def mock_driver():
    """Fixture to create a mocked WebDriver instance."""
    driver = MagicMock()
    return driver


@pytest.fixture
def login_dropdown_page(mock_driver):
    """Fixture to create a LoginDropdownPage instance with a mocked driver."""
    return LoginDropdownPage(driver=mock_driver)


def test_click_hudl(login_dropdown_page, mock_driver):
    """
    Test the `click_hudl` method.
    - Verifies the "Hudl" dropdown option is located using the correct locator.
    - Ensures the element's `click` method is called.
    - Confirms the method returns a `LoginPageWrapper` object.
    """
    # Mock the WebDriver's find_element method and the hudl option element it returns
    mock_hudl_option_element = MagicMock()
    mock_driver.find_element.return_value = mock_hudl_option_element

    # Call the method
    result = login_dropdown_page.click_hudl()

    # Assertions
    mock_driver.find_element.assert_called_once_with(*LoginDropdownPage.hudl_option)
    mock_hudl_option_element.click.assert_called_once()
    assert isinstance(result, LoginPageWrapper)
