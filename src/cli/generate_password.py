# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 9th, 2021

import random, array

length = int(input("Enter length: "))

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|',
'~', '>', '<', '*', '(', ')', '!', '^', '&', '_']

combined_list = digits + uppercase + lowercase + symbols

# Randomly select character from each array
rand_digit = random.choice(digits)
rand_upper = random.choice(uppercase)
rand_lower = random.choice(lowercase)
rand_symbol = random.choice(symbols)

temp_password = rand_digit + rand_upper + rand_lower + rand_symbol

# Fill password by selecting from combined list
for i in range(length - 4):
    temp_password = temp_password + random.choice(combined_list)

    temp_password_list = array.array('u', temp_password)

    random.shuffle(temp_password_list)

# Traverse temporary password and append charts
password = ""

for i in temp_password_list:
    password = password + i

print(f"Generated password: {password}")
