# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 7th, 2021

import random, time

heads_choice = "heads"
tails_choice = "tails"

flip_again = "yes"

# Flip the coin
while flip_again == "yes" or flip_again == "Yes" or flip_again == "y" or flip_again == "Y":
    print("Flipping the coin..")

    time.sleep(2)

    print("Flipped the coin. Result is", [heads_choice, tails_choice][random.randint(0, 1)])

    # FLip the coin again
    flip_again = input("Flip again (y/n)? ")

# If response is no, stop flipping
while flip_again == "no" or flip_again == "No" or flip_again == "n" or flip_again == "N":
    print("Flipping stopped.")

# If response is none of the above, stop program
else:
    print("Invalid response.")
