# chapters/multiplayer_game/server.py

import socket
from .protocol import send_msg, recv_msg
from chapters.my_tic_tac_toe.board import init_board, render
from chapters.my_tic_tac_toe.win import check_winner, is_tie
from chapters.my_tic_tac_toe.input_handler import get_move

HOST = ''
PORT = 9999

def main(screen=None):
    board = init_board()
    server_sock = socket.socket()

    server_sock.bind((HOST, PORT))
    server_sock.listen(1)
    print(f"Server listening on port {PORT}...")
    conn, addr = server_sock.accept()
    
    print("Client connected:", addr)

    try:
        # Server (X) makes the first move:
        render(board)
        r, c = get_move(board, 'X')
        board[r][c] = 'X'
        print("Your move:")
        render(board)

        # Send the updated board to the client so they can play O
        send_msg(conn, {'type': 'your_turn', 'board': board})

        while True:
            # 1) Receive O’s move from client
            msg = recv_msg(conn)
            if msg['type'] == 'move':
                r, c = msg['data']
                if board[r][c] != ' ':
                    # invalid; ask them to try again
                    send_msg(conn, {'type': 'invalid_move'})
                    continue
                board[r][c] = 'O'
                print("Client's move:")
                render(board)

                # Check for win/tie after O
                if check_winner(board, 'O'):
                    send_msg(conn, {'type': 'game_over', 'winner': 'O', 'board': board})
                    print("O wins!")
                    break
                if is_tie(board):
                    send_msg(conn, {'type': 'game_over', 'winner': None, 'board': board})
                    print("Tie game!")
                    break

                # 2) Server (X) move
                r2, c2 = get_move(board, 'X')
                board[r2][c2] = 'X'
                print("Your move:")
                render(board)

                # Check for win/tie after X
                if check_winner(board, 'X'):
                    send_msg(conn, {'type': 'game_over', 'winner': 'X', 'board': board})
                    print("X wins!")
                    break
                if is_tie(board):
                    send_msg(conn, {'type': 'game_over', 'winner': None, 'board': board})
                    print("Tie game!")
                    break

                # 3) Send updated board back for next O turn
                send_msg(conn, {'type': 'your_turn', 'board': board})

            elif msg['type'] == 'quit':
                break

    finally:
        conn.close()
        server_sock.close()
        print("Game ended")
