board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

p=1

def CreateBoard():
    print(" %c | %c | %c "%(board[1],board[2],board[3]))
    print("---|---|---")
    print(" %c | %c | %c "%(board[4],board[5],board[6]))
    print("---|---|---")
    print(" %c | %c | %c "%(board[7],board[8],board[9]))

def emptyPosition(a):
    if board[a]==" ":
        return True
    else:
        print("Choose the valid positionnn!!!!!!")

win='win'
draw='draw'
game=0

def CheckWin():
    global game
    if(board[1]==board[2] and board[2]==board[3] and board[1]!=' '):
        game=win
    elif(board[4]==board[5] and board[5]==board[6] and board[4]!=' '):
        game=win
    elif(board[7]==board[8] and board[8]==board[9] and board[7]!=' '):
        game=win
    elif(board[1]==board[4] and board[4]==board[7] and board[1]!=' '):
        game=win
    elif(board[2]==board[5] and board[5]==board[8] and board[2]!=' '):
        game=win
    elif(board[3]==board[6] and board[6]==board[9] and board[3]!=' '):
        game=win
    elif(board[1]==board[5] and board[5]==board[9] and board[1]!=' '):
        game=win
    elif(board[3]==board[5] and board[5]==board[7] and board[3]!=' '):
        game=win
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        game=draw
    else:
        game=0


while(game==0):
    CreateBoard()
    if p%2!=0:
        print("Player 1 have to mark'X'")
        mark='X'
    else:
        print("Player 2 have to mark'O'")
        mark='O'

    chose=int(input("Enter position: "))
    if(emptyPosition(chose)):
        board[chose]=mark
        p=p+1
        CheckWin()

if game==draw:
    print("game draww")
elif game==win:
    p=p-1
    if p%2!=0:
        print("player with 'X' mark win")
    else:
        print("player with 'O' mark winnnn")