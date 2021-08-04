'''
Developed by: Calinescu Mihai
Date: Mar, 2021

Github: https://github.com/CMihai99
'''


# Import Required Package
import time

answer = input("Would you like to play? (yes/no) ")

if answer.lower().strip() == "yes":
    time.sleep(0.2)
    print("You take a trip to the beach, and you want to enter the water.")
    time.sleep(2.8)
    answer = input("You hear people talking about a shark being in the water. Do you still enter the water or do other activities? (enter the water/do other activities) ").lower().strip()
    # Do you still enter the water or do other activities? enter the water/do other activities
    if answer == "enter the water":
        time.sleep(0.2)
        answer = input("You go into the water, have a good time, but after some time you hear a man screaming for help. Do you go investigate or do you leave immediately? (go investigate/leave immediately) ")
        if answer == "go investigate":
            time.sleep(0.2)
            print("You investigate, see the man, approach him, but find out he was eaten by the shark.")
            time.sleep(3.6)
            answer = input("Do you go look for help or mind your business and let other people deal with it? (look for help/mind my business) ")

            if answer == "mind my business":
                time.sleep(0.2)
                print("Too bad! You lost!")

            elif answer == "look for help":
                time.sleep(0.2)
                print("You go look for help and leave immediately. You won!")

        else:
            time.sleep(0.2)
            print("Too bad! You lost!")
            time.sleep(1.5)

    # Do you still enter the water or do other activities? do other activities
    elif answer == "do other activities":
        time.sleep(0.2)
        print("Needs work")

    else:
        time.sleep(0.2)
        print("Invalid choice, you lost!")

# Would you like to play? no
elif answer == "no":
    time.sleep(0.2)
    print("Too bad! You lost!")

else:
    time.sleep(0.2)
    print("Invalid choice, you lost!")