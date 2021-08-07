# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 7th, 2021

import random, time

heads_choice = "heads"
tails_choice = "tails"

flip_result = [heads_choice, tails_choice][random.randint(0, 1)]
flip_again = "yes"

# Flip the coin
if flip_again == "yes" or flip_again == "Yes" or flip_again == "y" or flip_again == "Y":
    print("Flipping the coin..")

    time.sleep(2)

    print(f"Flipped the coin. Result is {flip_result}")
