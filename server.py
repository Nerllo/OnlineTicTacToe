import socket
import threading
import time

HOST = 'localhost'
PORT = 8080

def player_turn(board, mark, conn, addr):
    conn.send(b"\nIt is your turn. Select the position you want to mark: ")
    while True:
        option_raw = conn.recv(1024)
        if option_raw:
            if option_raw.decode("utf-8") in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] and option_raw.decode("utf-8") not in ["|", "-", "X", "O"] and board.find(option_raw.decode("utf-8")) != -1:
                break
            else:
                conn.send(b"\nThat position is either taken or your input was invalid. Please try again: ")
    return board.replace(option_raw.decode("utf-8"), mark)

def client_interaction(conn, addr, conn2, addr2):
    with conn and conn2:
        mark = "O"
        mark2 = "X"
        board = "\n 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 \n"
        conn.send(b"Everyone is in! Ready to start the game. Player's 1 mark will be O and Player's 2 mark will be X.\n")
        conn2.send(b"Everyone is in! Ready to start the game. Player's 1 mark will be O and Player's 2 mark will be X.\n")
        while True:

            p1 = "Current board: (Player's 1 turn)" + board
            conn.send(p1.encode())
            conn2.send(p1.encode())
            board = player_turn(board, mark, conn, addr)

            
            if (board[2] == board[6] and board[6] == board[10]) or (board[30] == board[26] and board[26] == board[34]) or (board[50] == board[54] and board[54] == board[58]) or (board[2] == board[26] and board[26] == board[50]) or (board[6] == board[30] and board[30] == board[54]) or (board[10] == board[34] and board[34] == board[58]) or (board[2] == board[30] and board[30] == board[58]) or (board[10] == board[30] and board[30] == board[50]):
                conn.send(board.encode())
                conn2.send(board.encode())
                conn.send(b"\nPlayer 1 wins!")
                conn2.send(b"\nPlayer 1 wins!")
                break

            if board.find("1") == -1 and board.find("2") == -1 and board.find("3") == -1 and board.find("4") == -1 and board.find("5") == -1 and board.find("6") == -1 and board.find("7") == -1 and board.find("8") == -1 and board.find("9") == -1:
                conn.send(board.encode())
                conn2.send(board.encode())
                conn.send(b"\nIt is a tie!")
                conn2.send(b"\nIt is a tie!")
                break

            p2 = "Current board: (Player's 2 turn)" + board
            conn.send(p2.encode())
            conn2.send(p2.encode())
            board = player_turn(board, mark2, conn2, addr2)

            
            if (board[2] == board[6] and board[6] == board[10]) or (board[30] == board[26] and board[26] == board[34]) or (board[50] == board[54] and board[54] == board[58]) or (board[2] == board[26] and board[26] == board[50]) or (board[6] == board[30] and board[30] == board[54]) or (board[10] == board[34] and board[34] == board[58]) or (board[2] == board[30] and board[30] == board[58]) or (board[10] == board[30] and board[30] == board[50]):
                conn.send(board.encode())
                conn2.send(board.encode())
                conn.send(b"\nPlayer 2 wins!")
                conn2.send(b"\nPlayer 2 wins!")
                break

            if board.find("1") == -1 and board.find("2") == -1 and board.find("3") == -1 and board.find("4") == -1 and board.find("5") == -1 and board.find("6") == -1 and board.find("7") == -1 and board.find("8") == -1 and board.find("9") == -1:
                conn.send(board.encode())
                conn2.send(board.encode())
                conn.send(b"\nIt is a tie!")
                conn2.send(b"\nIt is a tie!")
                break
    print("GAME OVER")
    conn.close()
    conn2.close()

print("The server is now running\nWaiting for connections.\nTo stop the server please press CTRL + C")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        conn.send(b"You will be player 1. Waiting for a someone to join.\n")
        conn2, addr2 = s.accept()
        conn2.send(b"You will be player 2.\n")
        print("GAME STARTED")
        thread = threading.Thread(target = client_interaction, args = (conn, addr, conn2, addr2))
        thread.start()
    s.close()




