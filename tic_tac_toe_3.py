
def createBoard():
    board = [
        [" "," ", " "],
        [" "," ", " "],
        [" "," ", " "],
    ]
    return board

def printBoard(board):
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")

def userMove(board, player):
    move = input("Enter your move (1-9): ")
    if move == "1":
        board[0][0] = player
    elif move == "2":
        board[0][1] = player
    elif move == "3": 
        board[0][2] = player
    elif move == "4":
        board[1][0] = player
    elif move == "5":
        board[1][1] = player
    elif move == "6":
        board[1][2] = player
    elif move == "7":
        board[2][0] = player
    elif move == "8":
        board[2][1] = player
    elif move == "9":
        board[2][2] = player
    else:
        print("Wrong ...")

board = createBoard()
printBoard(board)
