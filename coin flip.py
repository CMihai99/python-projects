'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''


import random

user_input = int(input("Enter number of times to flip coin: "))

coin_choices = ('heads', 'tails')
coin_flips = []

for i in range(user_input): # FLips coin x number of times depending on user input
    coin_flip = random.choice(coin_choices)
    coin_flips.append(coin_flip)

print(coin_flips)
print(coin_flips.count('tails'), "tails")
print(coin_flips.count('heads'), "heads")