'''
Developed by: Calinescu Mihai
Date: 17 Mar, 2021

Github: https://github.com/CMihai99
'''


# 1. Initialize string data
string_data = input("Enter string: ")

# 2. Convert string data to binary data
res = ''.join(format(ord(i), '08b') for i in string_data)

# 3. Print result
print("Binary value after conversion: " + str(res)) 
