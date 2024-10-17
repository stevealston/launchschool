import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
MATCH_WIN = 3

def display_board(board):
    os.system('clear')

    print(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print("     |     |")
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print("     |     |")
    print("-----+-----+-----")
    print("     |     |")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print("     |     |")
    print("-----+-----+-----")
    print("     |     |")
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print("     |     |")
    print()

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def prompt(msg):
    print(f"==> {msg}")

def empty_squares(board):
    return [key
            for key, value in board.items()
            if value == INITIAL_MARKER]

def join_or(choices, delimiter=",", conjunction="or"):
    return f"{delimiter.join(choices[:-1]) + delimiter + conjunction + ' ' + choices[-1]}"
def player_choice(board):

    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square {join_or(valid_choices, '; ', 'and')}")
        square = int(input().strip())

        if square in empty_squares(board):
            break
        
        prompt('Sorry, that\'s not a valid choice.')
    
    board[square] = HUMAN_MARKER

def computer_choice(board):    
    if len(empty_squares(board)) == 0:
        return
    
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))


def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # cols
        [1, 5, 9], [3, 5, 7]              # diagonals
    ]

    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif(board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
        
    return None


def play_tic_tac_toe():
    while True:
        board = initialize_board()
        while True:
            display_board(board)

            player_choice(board)
            if someone_won(board) or board_full(board):
                break
            
            computer_choice(board)
            if someone_won(board) or board_full(board):
                break

        if someone_won(board):
          prompt(f"{detect_winner(board)} won!")
        else:
            prompt("It's a tie!")

        prompt("Play again? (y or n)")
        answer = input().lower()

        if answer[0] != 'y':
            break
    prompt('Thanks for playing Tic Tac Toe!')

play_tic_tac_toe()