'''
Developed by: Calinescu Mihai
Date: 14 Mar, 2021

Github: https://github.com/CMihai99
'''


import random

# Guess The Number
def guess_number(x):
    random_number = random.randint(1, x)
    guess_number = 0

    while guess_number != random_number:
        guess_number = int(input(f'Guess a number between 1 and {x}: '))
        if guess_number < random_number:
            print('Too low, guess again!')
        elif guess_number > random_number:
            print('Too high, guess again!')

    print(f'Congratulations! You have guessed the number {random_number} correctly!')

# Set maximum range
guess_number(int(input("Enter range: ")))