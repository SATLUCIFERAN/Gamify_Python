# chapters/multiplayer_game/client.py

import socket
from .protocol import send_msg, recv_msg
from chapters.my_tic_tac_toe.board import render
from chapters.my_tic_tac_toe.input_handler import get_move

HOST = 'localhost'
PORT = 9999

def main(screen=None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    print(f"Connected to server at {HOST}:{PORT}")

    try:
        while True:
            msg = recv_msg(sock)

            if msg['type'] == 'your_turn':
                board = msg['board']
                render(board)

                # Get O’s move and send it
                r, c = get_move(board, 'O')
                send_msg(sock, {'type': 'move', 'data': (r, c)})

                # Immediately show the board with your move
                board[r][c] = 'O'
                print("Your move:")
                render(board)

            elif msg['type'] == 'invalid_move':
                print("That square’s taken—try again.")

            elif msg['type'] == 'game_over':
                if 'board' in msg:
                    render(msg['board'])
                winner = msg.get('winner')
                print(f"\nGame over! {'Tie!' if winner is None else f'Winner: {winner}'}")
                break

    finally:
        sock.close()
        print("Connection closed")
