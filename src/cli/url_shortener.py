'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''

import pyshorteners

# Create URL Shortener Process
link = input("Enter The URL: ")
shortener = pyshorteners.Shortener()
new_url = shortener.tinyurl.short(link)

print(new_url)
