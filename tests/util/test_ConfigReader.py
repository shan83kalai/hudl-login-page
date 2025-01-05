from unittest.mock import patch

import pytest
from cryptography.fernet import Fernet

from util.ConfigReader import ConfigReader


@pytest.fixture
def valid_config_data():
    """Fixture to provide valid mocked configuration data."""
    # Generate a real secret key and encrypt a sample password with it
    secret_key = Fernet.generate_key()
    fernet = Fernet(secret_key)
    encrypted_password = fernet.encrypt("test_password".encode()).decode()

    # Return mock config data
    return {
        "DEFAULT": {
            "SECRET_KEY": secret_key.decode(),  # Real key as string
            "ENCRYPTED_PASSWORD": encrypted_password,  # Encrypted password as string
        }
    }


def test_get_config():
    """
    Test the `get_config` method.
    - Ensures that the method reads the correct config file.
    """
    with patch("os.path.join", return_value="mocked/config/path/Constants.properties") as mock_join, \
            patch("os.path.dirname", return_value="mocked_dir"):
        # Call the method
        config = ConfigReader.get_config()

        # Assertions
        mock_join.assert_called()  # Ensures path construction is called
        assert config is not None, "ConfigReader should return a valid ConfigParser object."


def test_get_password(valid_config_data):
    """
    Test the `get_password` method.
    - Ensures that the encrypted password is decrypted correctly.
    """
    # Use the valid_config_data fixture with known values
    secret_key = valid_config_data["DEFAULT"]["SECRET_KEY"]
    encrypted_password = valid_config_data["DEFAULT"]["ENCRYPTED_PASSWORD"]

    # Mock the configuration using the real values
    config_mock = {
        "DEFAULT": {
            "SECRET_KEY": secret_key,
            "ENCRYPTED_PASSWORD": encrypted_password,
        }
    }

    # Call the method
    decrypted_password = ConfigReader.get_password(config_mock)

    # Assertions
    assert decrypted_password == "test_password", "Decrypted password should match the original."


def test_invalid_decryption_key(valid_config_data):
    """
    Test the `get_password` method with an invalid SECRET_KEY.
    - Ensure that decryption raises an exception if the key is invalid.
    """
    invalid_secret_key = Fernet.generate_key()  # Generate a random invalid key

    # Mock the configuration with the wrong key
    config_mock = {
        "DEFAULT": {
            "SECRET_KEY": invalid_secret_key.decode(),  # Invalid key
            "ENCRYPTED_PASSWORD": valid_config_data["DEFAULT"]["ENCRYPTED_PASSWORD"],
        }
    }

    # Expect a decryption failure
    with pytest.raises(Exception):
        ConfigReader.get_password(config_mock)  # This should fail decryption
