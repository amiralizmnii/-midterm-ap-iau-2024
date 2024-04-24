
def createBoard():
    board = [
        ["x"," ", " "],
        [" "," ", " "],
        [" "," ", "o"],
    ]
    return board

def printBoard(board):
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")



board = createBoard()
printBoard(board)
print(board[0][0])