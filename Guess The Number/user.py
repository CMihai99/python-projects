'''
Developed by: Calinescu Mihai
Date: 14 Mar, 2021

Github: https://github.com/CMihai99
'''


import random

# Guess The Number
def computer_guess_number(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess_number = random.randint(low, high)
        else:
            guess = low # could also be high because low = high
        feedback = input(f'Is {guess_number} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'h':
            high = guess_number - 1
        if feedback == 'l':
            low = guess_number + 1

    print(f'The Computer has guessed your number, {guess_number}, correctly!')

# Set maximum range
computer_guess_number(500)
