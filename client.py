import socket
import random
import os.path

HOST = 'localhost'
PORT = 8080

def multiplayer():
    print("\nWelcome to the PvP mode.\n\n")

    file_name_int = 1
    file_name = str(file_name_int) + ".txt"
    while os.path.exists(file_name) == True:
        file_name_int = file_name_int + 1
        file_name = str(file_name_int) + ".txt"
    f = open(file_name,"w+")
    f.write("\nREPLAY (PvP):\n")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            raw_data = ""
            raw_data = s.recv(1024)
            if raw_data:
                print(raw_data.decode("utf-8"))
            if (raw_data.decode("utf-8")).find("\nIt is your turn. Select the position you want to mark: ") != -1 or (raw_data.decode("utf-8")).find("\nThat position is either taken or your input was invalid. Please try again: ") != -1:
                option = input("mark position: ")
                while option not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    option = input("Invalid input, please try again: ")
                s.send(option.encode())
            else: 
                f.write(raw_data.decode("utf-8"))
            if (raw_data.decode("utf-8")).find("\nPlayer 2 wins!") != -1 or (raw_data.decode("utf-8")).find("\nPlayer 1 wins!") != -1 or (raw_data.decode("utf-8")).find("\nIt is a tie!") != -1:
                break
        s.close()
        print("To watch the replay of this game insert the number ", file_name_int, " in the replay option.")
        print("Thank you for playing")
        f.write("\nEND OF THE REPLAY.")
        f.close()

def player_turn(board, mark, f):
    f.write("Current board: (Your Turn)" + board)
    print("Current board: (Your Turn)" + board)
    option = input("It is your turn. Select the position you want to mark: ")
    while option not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or option in ["|", "-", "X", "O"] or board.find(option) == -1:
        option = input("\nThat position is either taken or your input was invalid. Please try again: ")
    return board.replace(option, mark)

def computer_turn(board, mark, f):
    f.write("Current board: (Computer's Turn)" + board)
    print("\nCurrent board: (Computer's Turn)" + board)
    choice = random.randint(1,9)
    while board.find(str(choice)) == -1:
        choice = random.randint(1,9)
    return board.replace(str(choice), mark)

def game():
    board = "\n 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 \n"

    file_name_int = 1
    file_name = str(file_name_int) + ".txt"
    while os.path.exists(file_name) == True:
        file_name_int = file_name_int + 1
        file_name = str(file_name_int) + ".txt"
    f = open(file_name,"w+")
    f.write("\nREPLAY (PvE):\n")

    print("\nWelcome to the PvE mode.\n\n")
    mark = input("Do you want to be O or X: ")
    mark = mark.upper()
    while mark not in ["O", "X"]:
        mark = input("Wrong input. Please input X or O: ")
        mark = mark.upper()
    if mark == "O":
        computers_mark = "X"
    else:
        computers_mark = "O"
    turn = input("Do you want to play 'first' or 'second': ")
    while turn not in ["first", "second"]:
        turn = input("Wrong input. Please input 'first' or 'second': ")
    f_mark = "You are " + mark + "\n"
    f.write(f_mark)
    if turn == "first":
        while True:
            board = player_turn(board, mark, f)
            
            if (board[2] == board[6] and board[6] == board[10]) or (board[30] == board[26] and board[26] == board[34]) or (board[50] == board[54] and board[54] == board[58]) or (board[2] == board[26] and board[26] == board[50]) or (board[6] == board[30] and board[30] == board[54]) or (board[10] == board[34] and board[34] == board[58]) or (board[2] == board[30] and board[30] == board[58]) or (board[10] == board[30] and board[30] == board[50]):
                f.write(board)
                f.write("\nYou win!")
                print(board)
                print("\nYou win!")
                break

            if board.find("1") == -1 and board.find("2") == -1 and board.find("3") == -1 and board.find("4") == -1 and board.find("5") == -1 and board.find("6") == -1 and board.find("7") == -1 and board.find("8") == -1 and board.find("9") == -1:
                f.write(board)
                f.write("The match is a tie!")
                print(board)
                print("The match is a tie!")
                break

            board = computer_turn(board, computers_mark, f)

            if (board[2] == board[6] and board[6] == board[10]) or (board[30] == board[26] and board[26] == board[34]) or (board[50] == board[54] and board[54] == board[58]) or (board[2] == board[26] and board[26] == board[50]) or (board[6] == board[30] and board[30] == board[54]) or (board[10] == board[34] and board[34] == board[58]) or (board[2] == board[30] and board[30] == board[58]) or (board[10] == board[30] and board[30] == board[50]):
                f.write(board)
                f.write("\nYou lose!")
                print(board)
                print("\nYou lose")
                break

            if board.find("1") == -1 and board.find("2") == -1 and board.find("3") == -1 and board.find("4") == -1 and board.find("5") == -1 and board.find("6") == -1 and board.find("7") == -1 and board.find("8") == -1 and board.find("9") == -1:
                f.write(board)
                f.write("The match is a tie!")
                print(board)
                print("The match is a tie!")
                break
    
    if turn == "second":
        while True:
            board = computer_turn(board, computers_mark, f)

            if (board[2] == board[6] and board[6] == board[10]) or (board[30] == board[26] and board[26] == board[34]) or (board[50] == board[54] and board[54] == board[58]) or (board[2] == board[26] and board[26] == board[50]) or (board[6] == board[30] and board[30] == board[54]) or (board[10] == board[34] and board[34] == board[58]) or (board[2] == board[30] and board[30] == board[58]) or (board[10] == board[30] and board[30] == board[50]):
                f.write(board)
                f.write("\nYou lose!")
                print(board)
                print("\nYou lose")
                break

            if board.find("1") == -1 and board.find("2") == -1 and board.find("3") == -1 and board.find("4") == -1 and board.find("5") == -1 and board.find("6") == -1 and board.find("7") == -1 and board.find("8") == -1 and board.find("9") == -1:
                f.write(board)
                f.write("The match is a tie!")
                print(board)
                print("The match is a tie!")
                break
            
            board = player_turn(board, mark, f)
            
            if (board[2] == board[6] and board[6] == board[10]) or (board[30] == board[26] and board[26] == board[34]) or (board[50] == board[54] and board[54] == board[58]) or (board[2] == board[26] and board[26] == board[50]) or (board[6] == board[30] and board[30] == board[54]) or (board[10] == board[34] and board[34] == board[58]) or (board[2] == board[30] and board[30] == board[58]) or (board[10] == board[30] and board[30] == board[50]):
                f.write(board)
                f.write("\nYou win!")
                print(board)
                print("\nYou win!")
                break

            if board.find("1") == -1 and board.find("2") == -1 and board.find("3") == -1 and board.find("4") == -1 and board.find("5") == -1 and board.find("6") == -1 and board.find("7") == -1 and board.find("8") == -1 and board.find("9") == -1:
                f.write(board)
                f.write("The match is a tie!")
                print(board)
                print("The match is a tie!")
                break
    print("To watch the replay of this game insert the number ", file_name_int, " in the replay option.")
    print("Thank you for playing")
    f.write("\nEND OF THE REPLAY.")
    f.close()
            
def replay_menu():
    replay_number = input("Please input the unique number of the replay you want to see, or type '0' to go back to the main menu: ")
    if str(replay_number) == '0':
            return
    replay = str(replay_number) + ".txt"
    while os.path.exists(replay) == False:
        replay_number = input("There is no replay associated with your input, please try again. You can type '0' to go back to the main manu ")
        if str(replay_number) == '0':
            return
        replay = str(replay_number) + ".txt"
    f = open(replay, "r")
    r = f.read()
    print(r)
    f.close()

# Reminder
# board[2] = 1
# board[6] = 2
# board[10] = 3
# board[26] = 4
# board[30] = 5
# board[34] = 6
# board[50] = 7
# board[54] = 8
# board[58] = 9

print("Welcome to TIC TAC TOE\n")
while True:
    print("\nPlease select one of the following options by inputting the number:\n")
    print("1. Single Player (PvE)")
    print("2. Online Multiplayer (PvP)")
    print("3. Look at a replay")
    print("4. Exit")
    
    option = input("Option: ")
    while option not in ["1", "2", "3", "4"]:
        option = input("Wrong input, try again: ")

    if option == "1":
        game()
    
    if option == "2":
        multiplayer()

    if option == "3":
        replay_menu()

    if option == "4":
        break