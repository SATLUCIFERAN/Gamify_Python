def init_board():
    pass
def check_winner():
    pass

b = init_board()          # empty 3×3 board
b[2][2] = "O"             # place an O in bottom-right
assert check_winner(b, "O") is False, "O shouldn't win yet"


