
# game.py
from board         import init_board, render
from win           import check_winner, is_tie
from input_handler import get_move
from utils         import clear_screen

def main():
    board   = init_board()   # 1) Create an empty 3×3 board
    current = "X"            # 2) X always starts

    while True:
        # 3) Refresh the screen and show the latest board
        clear_screen()
        render(board)

        # 4) Ask the current player for their move
        row, col = get_move(board, current)

        # 5) Place the player's symbol on the board
        board[row][col] = current

        # 6) Check whether this move just won the game
        if check_winner(board, current):
            clear_screen()
            render(board)
            print(f"🎉 Player {current} wins!")
            break

        # 7) Check for a tie (board full, no winner)
        if is_tie(board):
            clear_screen()
            render(board)
            print("🤝 It's a tie!")
            break

        # 8) Switch players: X→O or O→X
        current = "O" if current == "X" else "X"

if __name__ == "__main__":
    main()


    
