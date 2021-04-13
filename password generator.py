'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''


import random
import array

max_length = int(input("Enter length of desired password: "))

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
					'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|',
	   				'~', '>', '*', '(', ')', '<']

# Combine arrays
combined_list = digits + uppercase_letters + lowercase_letters + symbols

# Randomly select at least one character from each array
rand_digit = random.choice(digits)
rand_upper = random.choice(uppercase_letters)
rand_lower = random.choice(lowercase_letters)
rand_symbol = random.choice(symbols)

# Combine the character randomly-selected above
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

# Fill rest of the password length by selecting randomly from combined_list
for i in range(max_length - 4):
	temp_pass = temp_pass + random.choice(combined_list)
	# Convert temporary password into array and shuffle to prevent from having a consistent pattern
	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)

# Traverse the temporary password array and append the charts to form password
password = ""
for i in temp_pass_list:
		password = password + i

print(password)