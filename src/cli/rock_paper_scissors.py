# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 10th, 2021

import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

victories = {
    Action.Scissors: [Action.Paper],
    Action.Paper: [Action.Rock],
    Action.Rock: [Action.Scissors],
}

def user_selection():
    choices = [f"{action.name} ({action.value})" for action in Action]
    choices_str = ", ".join(choices)

    selection = int(input(f"Enter choice: {choices_str}: "))

    action = Action(selection)

    return action

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)

    action = Action(selection)

    return action

def determine_winner(user_action, computer_action):
    defeats = victories[user_action]

    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. Tie.")

    elif computer_action in defeats:
        print(f"{user_action.name} beats {computer_action.name}! You win.")

    else:
        print(f"{computer_action.name} beats {user_action.name}! You lose.")

# Invalid response
while True:
    try:
        user_action = user_selection()

    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"

        print("Invalid selection.")

        continue

    computer_action = get_computer_selection()

    determine_winner(user_action, computer_action)
