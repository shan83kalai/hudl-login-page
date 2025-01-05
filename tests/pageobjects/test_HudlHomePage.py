from unittest.mock import MagicMock

import pytest

from pageobjects.HudlHomePage import HudlHomePage


@pytest.fixture
def mock_driver():
    """Fixture to create a mocked WebDriver instance."""
    driver = MagicMock()
    return driver


@pytest.fixture
def hudl_home_page(mock_driver):
    """Fixture to create a HudlHomePage instance with a mocked driver."""
    return HudlHomePage(driver=mock_driver)


def test_get_display_user_name(hudl_home_page, mock_driver):
    """
    Test the `get_display_user_name` method.
    - Verifies that the display name is retrieved from the correct element.
    - Ensures the locator is used correctly.
    - Checks the returned value matches the expected text.
    """
    # Mock the WebDriver's find_element method and display element
    mock_display_element = MagicMock()
    mock_driver.find_element.return_value = mock_display_element

    # Define the expected display name text
    expected_display_name = "Test User"
    mock_display_element.text = expected_display_name

    # Call the method
    result = hudl_home_page.get_display_user_name()

    # Assertions
    mock_driver.find_element.assert_called_once_with(*HudlHomePage.display_name)
    assert result == expected_display_name
