# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 2nd, 2021

import random, time

min = 1
max = 6

roll_again = "yes"

# Roll the dices
while roll_again == "yes" or roll_again == "Yes" or roll_again == "y" or roll_again == "Y":
    print("Rolling the dices..")

    time.sleep(3)

    print("Rolled the dices. Values are", random.randint(min, max), "and", random.randint(min, max))

    # Roll the dices again
    roll_again = input("Roll again (y/n)? ")

# If response is no, stop flipping
while flip_again == "no" or flip_again == "No" or flip_again == "n" or flip_again == "N":
    print("Rolling stopped.")

# If response is none of the above, stop program
else:
    print("Invalid response.")
