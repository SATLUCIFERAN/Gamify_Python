
# win.py

def check_winner(board, symbol):
    size = len(board)

    # 1) Horizontal
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    # 2) Vertical
    for col in range(size):
        if all(board[row][col] == symbol for row in range(size)):
            return True

    # 3) Diagonals
    if all(board[i][i] == symbol for i in range(size)):
        return True
    if all(board[i][size - 1 - i] == symbol for i in range(size)):
        return True

    # No winning condition met
    return False



def is_tie(board):
    # If any cell is still " ", it’s not a tie.
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    # No empty cells found — it’s a tie
    return True


def is_tie(board):
    return all(cell != " " for row in board for cell in row)

