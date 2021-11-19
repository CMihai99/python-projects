# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: November 19th, 2021

# Initialize string data
string_data = input("Enter string: ")

# Convert string data to binary data
res = ''.join(format(ord(i), '08b') for i in string_data)

print("Binary value after conversion: " + str(res)) 
