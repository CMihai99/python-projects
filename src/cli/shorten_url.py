# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 9th, 2021

import pyshorteners

url = input("Enter URL: ")

shortener = pyshorteners.Shortener()

shortened_url = shortener.tinyurl.short(url)

print(f"Shortened URL: {shortened_url}")
