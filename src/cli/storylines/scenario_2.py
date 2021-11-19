# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: November 19th, 2021

import time

answer = input("Would you like to play? ")

# Would you like to play? yes
if answer.lower().strip() == "yes" or "y":
    time.sleep(0.2)
    print("You take a trip to the beach, and you want to enter the water.")
    time.sleep(2.8)
    answer = input("You hear people talking about a shark being in the water. Do you still enter the water? ").lower().strip()
    # Do you still enter the water? yes
    if answer == "yes" or "y":
        time.sleep(0.2)
        answer = input("You go into the water, have a good time, but after some time you hear a man screaming for help. Do you go investigate or do you leave immediately? (go investigate/leave immediately) ")
        if answer == "go investigate":
            time.sleep(0.2)
            print("You investigate, see the man, approach him, but find out he was attacked by the shark.")
            time.sleep(3.6)
            answer = input("Do you go look for help or do you let other people deal with it? (look for help/let other people deal with it) ")

            if answer == "look for help":
                time.sleep(0.2)
                print("You go look for help and leave immediately. You won!")

            elif answer == "let other people deal with it":
                time.sleep(0.2)
                print("Too bad, you lost!")

        else:
            time.sleep(0.2)
            print("Too bad! You lost!")
            time.sleep(1.5)

    else:
        time.sleep(0.2)
        print("You enter the water and get attacked by the shark. You lost!")

# Would you like to play? no
if answer.lower().strip() == "no" or "n":
    time.sleep(0.2)
    print("Too bad, you lost!")

# Would you like to play? invalid answer
else:
    time.sleep(0.2)
    print("Invalid answer, you lost!")
