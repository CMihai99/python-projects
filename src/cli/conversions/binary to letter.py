# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: November 19th, 2021

# Convert to decimal
def binaryToDecimal(binary): 
    string = int(binary, 2) 
    return string

# Initialize binary data
binary_data = input("Enter binary data: ")

# Initialize empty string for storing the data
letter_data = ''

# Slice the input data and convert it to decimal and then convert to string
for i in range(0, len(binary_data), 7):
    # Slice binary_data  from index range [0, 6] and store it in temp_data
    temp_data = binary_data[i:i+7]

    # Pass temp_data in binaryToDecimal() function
    # to get decimal value of corresponding temp_data
    decimal_data = binaryToDecimal(temp_data)

    # Decode decimal value returned by binaryToDecimal() function,
    # using chr() function which returns the string's corresponding
    # character for given ASCII value, and store it in letter_data
    letter_data = letter_data + chr(decimal_data)

print("Letter value after conversion:", letter_data)
