from cryptography.fernet import Fernet

# Create a random key 
key = Fernet.generate_key()
print(f"Secret key (save securely, e.g., environment variables): {key.decode()}")

# Encrypt the password
fernet = Fernet(key)
password = "your_actual_password_here"
encrypted_password = fernet.encrypt(password.encode())
print(f"Encrypted Password: {encrypted_password.decode()}")