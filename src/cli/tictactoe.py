# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: September 1st, 2021

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True
winner = None
current_player = "X"

def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def play_game():
    display_board()

    while game_still_going:
        # Handle arbitrary player turn
        handle_turn(current_player)
        check_if_game_over()
        # Flip turn
        flip_player()

    if winner == "X" or winner == "O":
        print(f"{winner} Won!")

    elif winner == None:
        print("Tie.")

def handle_turn(player):
    print("{player}'s turn.")
    position = input("Choose a position from 1 to 9: ")
    valid = False

    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Incorrect position. Choose from 1 to 9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True

        else:
            print("You can't mark there! Try again.")

    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diagonal_winner:
        winner = diagonal_winner

    else:
        winner = None

    return

def check_rows():
    global game_still_going

    # Check if any of the rows have all the same value and are not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any rows have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]

    elif row_2:
        return board[3]

    elif row_3:
        return board[6]

    return

def check_columns():
    global game_still_going

    # Check if any of the collumns have all the same value and are not empty
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any columns have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]

    elif column_2:
        return board[1]

    elif column_3:
        return board[2]

    return

def check_diagonals():
    global game_still_going

    # Check if any of the diagonals have all the same value (and are not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    # If any diagonals have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False

    if diagonal_1:
        return board[0]

    elif diagonal_2:
        return board[6]

    return

def check_if_tie():
    global game_still_going

    if "-" not in board:
        game_still_going = False

    return

# Change turns
def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"

    return

play_game()
