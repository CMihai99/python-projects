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
    answer = input("You reach a crossroad, would you like to go left or right? ").lower().strip()
    # You reach a crossroad, would you like to go left or right? left
    if answer == "left":
        time.sleep(0.2)
        answer = input("You encounter a monster, would you like to run or attack? ")
        if answer == "attack":
            time.sleep(0.2)
            print("Not the greatest idea, you lost!")

        else:
            time.sleep(0.2)
            print("Good choice, you escaped safely.")
            time.sleep(1.5)
            print("On the way home, you see a helpless bird which has fallen from a tree and injured himself.")
            time.sleep(3)
            answer = input("Will you take him to the vet or will you take care of him at home? (take him to the vet/take care of him) ")

            if answer == "take him to the vet":
                time.sleep(0.2)
                print("You took a trip to the vet and got him checked. The vet told you that he had broken his wing and needs to be taken care of.")
                time.sleep(4)
                answer = input("Do you let the vet take care of him or do you bring him home and help him yourself? (let the vet take care of him/bring him home) ")

            if answer == "take care of him":
                time.sleep(0.2)
                print("You brang the bird at home and took care of him. You won!")

            if answer == "let the vet take care of him":
                time.sleep(0.2)
                print("You left him in the care of the vet and took off. You lost!")

            if answer == "bring him home":
                time.sleep(0.2)
                print("You brang the bird at home and took care of him. You won!")

    # You reach a crossroad, would you like to go left or right? right
    elif answer == "right":
        time.sleep(0.2)
        print("You walk aimlessly to the right and fall on a patch of ice. You injure your leg and cannot continue. You lost!")

    else:
        time.sleep(0.2)
        print("Invalid choice, you lost!")

# Would you like to play? no
else:
    time.sleep(0.2)
    print("Too bad! You lost!")