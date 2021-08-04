# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 4th, 2021

from cryptography.fernet import Fernet

string = input("Enter string: ")

# Generate encrypting key
key = Fernet.generate_key()

# Fernet key class
key_class = Fernet(key)

# Encrypt string
encrypt_message = key_class.encrypt(string.encode())
print("Encrypted string:", encrypt_message)
