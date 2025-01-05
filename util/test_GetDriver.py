from unittest.mock import patch, MagicMock

from util.DriverSetup import DriverSetup


@patch("selenium.webdriver.Chrome")  # Mock the Chrome WebDriver
def test_get_driver(mock_webdriver):
    """
    Test the `get_driver` method to verify:
    - `webdriver.Chrome()` is called.
    - `maximize_window()` is called on the driver instance.
    """
    # Create a MagicMock instance to mock the WebDriver
    mock_driver_instance = MagicMock()
    mock_webdriver.return_value = mock_driver_instance

    # Call the method
    driver = DriverSetup.get_driver()

    # Assertions
    mock_webdriver.assert_called_once()  # Verify that webdriver.Chrome() was called
    mock_driver_instance.maximize_window.assert_called_once()  # Ensure maximize_window() is called
    assert driver == mock_driver_instance, "get_driver should return the mocked WebDriver instance."