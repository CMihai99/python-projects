'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''


import random, time

# Assign variables
min = 1
max = 6

roll_again = "yes"

# Roll the dices
while roll_again == "yes" or roll_again == "y" or roll_again == "Y" or roll_again == "Yes":
    print("Rolling the dices...")
    time.sleep(1)
    print("Following values are:", random.randint(min, max), "and", random.randint(min, max))

    # Roll the dices again
    roll_again = input("Roll again? ")

else:
    print("Process finished")
