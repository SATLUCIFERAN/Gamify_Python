
from win import check_winner, is_tie
from board import init_board

# Test a winning row:
b = init_board()
b[0] = ["X","X","X"]
assert check_winner(b, "X") is True

# Test a winning column:
b = init_board()
for r in range(3):
    b[r][1] = "O"
assert check_winner(b, "O") is True

# Test a diagonal:
b = init_board()
for i in range(3):
    b[i][i] = "X"
assert check_winner(b, "X") is True

# Test a tie:
b = [
  ["X","O","X"],
  ["O","X","O"],
  ["O","X","O"],
]
assert is_tie(b) is True
assert check_winner(b, "X") is False


