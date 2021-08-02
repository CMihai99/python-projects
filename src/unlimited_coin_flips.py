# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 2nd, 2021

import random, time

user_input = int(input("Enter number of times to flip coin: "))

coin_choices = ('heads', 'tails')
coin_flips = []

flip_again = "yes"

# If response is yes, start flipping
while flip_again == "yes" or flip_again == "Yes" or flip_again == "y" or flip_again == "Y":
    print("Flipping the coin", user_input, "times..")

    # Flip coin X number of times
    for i in range(user_input):
        coin_flip = random.choice(coin_choices)
        coin_flips.append(coin_flip)

    time.sleep(2)

    print("Flipped the coin. Values are", "heads", coin_flips.count('heads'), "times",
    "and", "tails", coin_flips.count('tails'), "times")

    # See each flip
    # print(coin_flips)

    # FLip the coin again
    flip_again = input("Flip again (y/n)? ")

# If response is no, stop flipping
while flip_again == "no" or flip_again == "No" or flip_again == "n" or flip_again == "N":
    print("Flipping stopped.")

# If response is none of the above, stop program
else:
    print("Invalid response.")
