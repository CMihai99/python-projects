# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 7th, 2021

from cryptography.fernet import Fernet

string = input("Enter string: ")

key = Fernet.generate_key()
key_class = Fernet(key)

# Encrypt string
encrypt_message = key_class.encrypt(string.encode())

print(f"Encrypted string: {encrypt_message}")
