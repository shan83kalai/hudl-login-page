import configparser
from cryptography.fernet import Fernet
import os


class ConfigReader:
    @staticmethod
    def get_config():
        # Read config file using the project directory
        config = configparser.ConfigParser()
        # Dynamically determine the project root and locate config directory
        current_dir = os.path.dirname(os.path.abspath(__file__))  # util
        project_dir = os.path.dirname(current_dir)  # Move up to project root
        config_dir = os.path.join(project_dir, "config")  # Move to config directory

        # Construct the full path to Constants.properties
        config_file_path = os.path.join(config_dir, "Constants.properties")

        # Read the config file
        config.read(config_file_path)
        return config

    @staticmethod
    def get_password(config):
        encrypted_password = config["DEFAULT"]["ENCRYPTED_PASSWORD"]
        secret_key = config["DEFAULT"]["SECRET_KEY"]
        fernet = Fernet(secret_key)
        return fernet.decrypt(encrypted_password.encode()).decode()
