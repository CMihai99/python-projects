'''
Developed by: Calinescu Mihai
Date: 17 Mar, 2021

Github: https://github.com/CMihai99
'''


# 1. Convert to decimal
def binaryToDecimal(binary): 
    string = int(binary, 2) 
    return string

# 2. Initialize binary data
binary_data = input("Enter binary data: ")

# 3. Initialize empty string for storing the data
letter_data = ''

# 4. Slice the input data and convert it to decimal and then convert to string
for i in range(0, len(binary_data), 7):
    # 5. Slice binary_data  from index range [0, 6] and store it in temp_data
    temp_data = binary_data[i:i+7]

    # 6. Pass temp_data in binaryToDecimal() function
    # to get decimal value of corresponding temp_data
    decimal_data = binaryToDecimal(temp_data)

    # 7. Decode decimal value returned by binaryToDecimal() function, using chr()
    # function which returns the string's corresponding character for given ASCII value,
    # and store it in letter_data
    letter_data = letter_data + chr(decimal_data)

# 8. Print result
print("Letter value after conversion:", letter_data)