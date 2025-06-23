# input_handler.py

from .utils import get_int

def get_move(board, player_symbol):
    
    size = len(board)
    
    while True:
        print(f"Player {player_symbol}, enter row and column (1–{size}):")

        # 1) Get row and column as integers
        row = get_int("  Row: ") - 1
        col = get_int("  Col: ") - 1

        # 2) Check bounds
        if not (0 <= row < size and 0 <= col < size):
            print(f"Coordinates must be between 1 and {size}. Try again.\n")
            continue

        # 3) Check if the cell is empty
        if board[row][col] != " ":
            print("That cell is already taken. Try again.\n")
            continue

        # 4) Valid move! Return zero-based indices
        return row, col

