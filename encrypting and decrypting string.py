'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''

import time
from cryptography.fernet import Fernet

string = input("Enter string: ")

key = Fernet.generate_key() # Generate encryption & decryption key using fernet

fernet = Fernet(key)        # Instance Fernet class with key

encMessage = fernet.encrypt(string.encode())  # Encrypt string
time.sleep(1)
print("") # Empty row for better visualization
print("Encrypted string:", encMessage)

decMessage = fernet.decrypt(encMessage).decode() # Decrypt encrypted string
time.sleep(1)
print("") # Empty row for better visualization
print("Decrypted string:", decMessage)