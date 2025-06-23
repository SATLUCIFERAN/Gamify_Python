


board = [
    ["X", " ", "O"],
    [" ", "X", " "],
    ["O", " ", "X"],
]


for row in board:
    line = " | ".join(row)
    print(line)

'''
X |   | O
  | X |
O |   | X

'''

for row in board:
    line = " " + " | ".join(row) + " "
    print(line)

'''
 X |   | O
   | X |
 O |   | X

'''

