from unittest.mock import MagicMock

import pytest

from pageobjects.HomePage import HomePage
from pageobjects.LoginDropdownPage import LoginDropdownPage


@pytest.fixture
def mock_driver():
    """Fixture to create a mocked WebDriver instance."""
    driver = MagicMock()
    return driver


@pytest.fixture
def home_page(mock_driver):
    """Fixture to create a HomePage instance with a mocked driver."""
    return HomePage(driver=mock_driver)


def test_click_login_button(home_page, mock_driver):
    """
    Test the click_login_button method of HomePage.
    - Verifies that it finds the correct element.
    - Ensures the `click` method is called on the login button.
    - Checks if the `LoginDropdownPage` is returned.
    """
    # Mock the WebDriver find_element method and click behavior
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element

    # Call the click_login_button method
    result = home_page.click_login_button()

    # Assertions
    mock_driver.find_element.assert_called_once_with(*HomePage.login_button)
    mock_element.click.assert_called_once()
    assert isinstance(result, LoginDropdownPage)
