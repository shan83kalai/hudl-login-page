import pytest
from cryptography.fernet import Fernet


def test_generate_key():
    """
    Test that a random key is generated and can be used for encryption and decryption.
    """
    # Generate a key
    key = Fernet.generate_key()

    # Assertions
    assert isinstance(key, bytes), "The key should be of type 'bytes'."
    assert len(key) > 0, "The key should not be empty."


def test_encryption_and_decryption():
    """
    Test the encryption and decryption of a password using Fernet.
    """
    # Generate a key
    key = Fernet.generate_key()
    fernet = Fernet(key)

    # Password to encrypt
    password = "your_test_password"

    # Encrypt the password
    encrypted_password = fernet.encrypt(password.encode())

    # Assertions on encryption
    assert isinstance(encrypted_password, bytes), "The encrypted password should be of type 'bytes'."
    assert encrypted_password != password.encode(), "The encrypted password should not match the original password."

    # Decrypt the password and validate it
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    assert decrypted_password == password, "The decrypted password does not match the original password."


def test_encryption_with_invalid_key():
    """
    Test that encryption fails if an invalid or mismatched key is used for decryption.
    """
    # Generate a key and create a Fernet instance
    key = Fernet.generate_key()
    fernet = Fernet(key)

    # Password to encrypt
    password = "your_test_password"

    # Encrypt the password
    encrypted_password = fernet.encrypt(password.encode())

    # Generate a new invalid key and create a new Fernet instance
    invalid_key = Fernet.generate_key()
    another_fernet = Fernet(invalid_key)

    # Assertions for decryption failure with invalid key
    with pytest.raises(Exception):
        another_fernet.decrypt(encrypted_password)