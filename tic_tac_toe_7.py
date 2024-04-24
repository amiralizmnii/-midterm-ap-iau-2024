# Game board - Game state

# our basic board

def createBoard():
    board = [
        [" "," ", " "],
        [" "," ", " "],
        [" "," ", " "],
    ]
    return board


# location of board

def printBoard(board):
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")

# User input for move in board 

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

# Check for which player is winner

def checkForWinner(board, player):
    # Check rows
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return player
    if board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return player
    if board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return player
    
    # Check cols
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return player
    if board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return player
    if board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return player
    
    # Check diags
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return player
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return player
    
    # Check if no one has won

    if board[0][0] != " " and board[0][1] != " " and board[0][2] != " " and board[1][0] != " " and board[1][1] != " " and board[1][2] != " " and board[2][0] != " " and board[2][1] != " " and board[2][2] != " " :
        return "No"


# Main program

board = createBoard()
printBoard(board)
player = "x"
winner = None

# Game loop

while winner == None:

    # Player Move 
    userMove(board, player)

    # Print boarder
    printBoard(board)

    # Check winner
    winner = checkForWinner(board, player)

    # switch player 
    if player == "x":
        player = "o"
    else:
        player = "x"


# result of game
if winner == "No" :
    print("Tie game :( ")
else:
    print(f'player "{winner}" has won the game :) ')