# hudl-login-page
# SecureConfig - Safeguard Your Sensitive Data

**SecureConfig** is a lightweight Python package designed to securely manage sensitive data such as passwords, API keys, and configuration settings using encryption. Built on the robust [cryptography](https://cryptography.io/en/latest/) library, SecureConfig ensures sensitive information is encrypted and protected, preventing accidental exposure in your code.

---

## **Features**
- Encrypt sensitive data (e.g., passwords, API keys, etc.).
- Decrypt previously encrypted values securely.
- Uses industry-standard AES encryption (via Fernet from the `cryptography` library).
- Simple interface for integration into Python projects.
- Environment-safe: store encryption keys securely in environment variables for added security.

---

## **Getting Started**

### **Prerequisites**
- Python 3.7 or higher
- Install the `cryptography` library:
  ```bash
  pip install cryptography
  ```

---

### **Installation**

Clone the repository or add the package to your project:

```bash
git clone https://github.com/shan83kalai/hudl-login-page.git
```

Alternatively, if published on PyPI:

```bash
pip install secureconfig
```

---

### **Usage**

#### **1. Generate a Secret Key**
This key is used for both encryption and decryption. Store it securely (e.g., in environment variables or a configuration file).

```python
from cryptography.fernet import Fernet

# Generate a random encryption key
key = Fernet.generate_key()
print(f"Secret key (save this securely!): {key.decode()}")
```

#### **2. Encrypt Sensitive Data**
Use the secret key to encrypt sensitive information.

```python
from cryptography.fernet import Fernet

# Initialize Fernet with your secret key
key = b"your_generated_key_here"  # Replace with your key
fernet = Fernet(key)

# Encrypt a password
password = "your_actual_password_here"
encrypted_password = fernet.encrypt(password.encode())
print(f"Encrypted Password: {encrypted_password.decode()}")
```

#### **3. Decrypt Previously Encrypted Data**
Retrieve the original sensitive value by decrypting it.

```python
# Decrypt the encrypted password
decrypted_password = fernet.decrypt(encrypted_password).decode()
print(f"Decrypted Password: {decrypted_password}")
```

---

### **Environment Variable Integration**

For added security, avoid hardcoding the encryption key in Python code. Instead, store the key as an environment variable and retrieve it when needed:

```python
import os
from cryptography.fernet import Fernet

# Fetch the key from environment variables
key = os.getenv("SECURE_CONFIG_KEY").encode()
fernet = Fernet(key)

# Encrypt/Decrypt sensitive data as usual
```

Set the environment variable on your system:
```bash
export SECURE_CONFIG_KEY=your_generated_key_here
```

---

## **Best Practices**
1. Always store the encryption key securely:
    - Use environment variables (e.g., `os.getenv()`).
    - Store it in a secure file that is excluded from version control (`.gitignore`).
2. Never expose the encryption key in your code.
3. Rotate and regenerate keys periodically for better security.

---

## **Contributing**

We welcome contributions! To contribute to SecureConfig:
1. Fork this repository.
2. Create a feature branch (`feature-branch-name`).
3. Commit your changes.
4. Create a pull request to the main branch.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contact**
For questions or issues, please contact:
- Name: Guljar Hussain
- Email: gz.hussain@gmail.com

---

## **Acknowledgments**
Built with the help of the [cryptography](https://cryptography.io/en/latest/) library.