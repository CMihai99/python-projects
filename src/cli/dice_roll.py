# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 7th, 2021

import random, time

min = 1
max = 6

roll_result = random.randint(min, max)
roll_again = "yes"

# Roll the dice
if roll_again == "yes" or roll_again == "Yes" or roll_again == "y" or roll_again == "Y":
    print("Rolling the dice..")

    time.sleep(2)

    print(f"Rolled the dice. Result is {roll_result}")
