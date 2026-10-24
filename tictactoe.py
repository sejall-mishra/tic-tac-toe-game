import random

HUMAN = "X"
COMPUTER = "O"

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
]


def show_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}      1 | 2 | 3")
    print("---+---+---    ---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}      4 | 5 | 6")
    print("---+---+---    ---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}      7 | 8 | 9")
    print()


def get_winner(board):
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board):
    return " " not in board


def available_moves(board):
    return [i for i, square in enumerate(board) if square == " "]


def human_move(board):
    while True:
        choice = input("Your move (1-9): ")
        if not choice.isdigit():
            print("Please type a number from 1 to 9.")
            continue
        position = int(choice) - 1
        if position < 0 or position > 8:
            print("Please type a number from 1 to 9.")
        elif board[position] != " ":
            print("That square is already taken.")
        else:
            board[position] = HUMAN
            return


def minimax(board, computer_turn):
    winner = get_winner(board)
    if winner == COMPUTER:
        return 1
    if winner == HUMAN:
        return -1
    if is_full(board):
        return 0

    if computer_turn:
        best = -2
        for move in available_moves(board):
            board[move] = COMPUTER
            best = max(best, minimax(board, False))
            board[move] = " "
        return best
    else:
        best = 2
        for move in available_moves(board):
            board[move] = HUMAN
            best = min(best, minimax(board, True))
            board[move] = " "
        return best


def best_move(board):
    best_score = -2
    chosen = None
    for move in available_moves(board):
        board[move] = COMPUTER
        score = minimax(board, False)
        board[move] = " "
        if score > best_score:
            best_score = score
            chosen = move
    return chosen


def computer_move(board, level):
    if level == "easy":
        move = random.choice(available_moves(board))
    else:
        move = best_move(board)
    board[move] = COMPUTER
    print(f"Computer plays {move + 1}")


def choose_level():
    while True:
        choice = input("Choose level: 1 = Easy, 2 = Unbeatable: ")
        if choice == "1":
            return "easy"
        if choice == "2":
            return "hard"
        print("Please type 1 or 2.")


def play_game():
    board = [" "] * 9
    level = choose_level()
    show_board(board)

    while True:
        human_move(board)
        show_board(board)
        if get_winner(board) == HUMAN:
            print("You win!")
            return
        if is_full(board):
            print("It's a draw!")
            return

        computer_move(board, level)
        show_board(board)
        if get_winner(board) == COMPUTER:
            print("Computer wins!")
            return
        if is_full(board):
            print("It's a draw!")
            return


def main():
    print("Welcome to Tic-Tac-Toe! You are X, the computer is O.")
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()