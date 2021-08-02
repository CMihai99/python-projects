'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''


from phonenumbers import geocoder
from phonenumbers import carrier

phone = input("Enter phone number (including prefix, no spaces): ") # Enter phone number

country = phonenumbers.parse(phone, "CH")
print("Country:", geocoder.description_for_number(country, "en")) # Print phone number country

carrier = phonenumbers.parse(phone, "RO")
print("Carrier:", carrier.name_for_number(carrier, "en")) # Print phone number carrier
