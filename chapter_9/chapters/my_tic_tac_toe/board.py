
# board.py

def init_board(size=3):
   
    return [[" " for _ in range(size)] for _ in range(size)]


def render(board):
  
    size = len(board)
    for row_index, row in enumerate(board):
        # Join the cell contents with ' | ' separators
        print(" " + " | ".join(row) + " ")
        # After each row except the last, print a horizontal divider
        if row_index < size - 1:
            print("---" + "+---" * (size - 1))

'''

board = [
    ["X", " ", "O"],
    [" ", "X", " "],
    ["O", " ", "X"],
]

render(board)



 X |   | O 
---+---+---
   | X |
---+---+---
 O |   | X



'''