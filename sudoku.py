b=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def createBoard():
    print(" ___ ___ ___ ")
    print("| %s | %s | %s |"%(b[1],b[2],b[3]))
    print("|___|___|___|")
    print("| %s | %s | %s |"%(b[4],b[5],b[6]))
    print("|___|___|___|")
    print("| %s | %s | %s |"%(b[7],b[8],b[9]))
    print("|___|___|___|")
game=0
win='win'
lose='lose'

def CheckPosition(x):
    if(b[x]==" "):
        return True
    else:
        print("Enter the value at valid position!!!!!!!!")
def checkWin():
    global game
    if(b[1]!=b[2]!=b[3] and b[4]!=b[5]!=b[6] and b[7]!=b[8]!=b[9] and b[1]!=b[4]!=b[7] and b[2]!=b[5]!=b[8] and b[3]!=b[6]!=b[9]
    and b[1]!=' 'and b[2]!=' 'and b[3]!=' 'and b[4]!=' 'and b[5]!=' 'and b[6]!=' 'and b[7]!=' 'and b[8]!=' 'and b[9]!=' '):
        game=win
    elif((b[1]==b[2] or b[1]==b[3] or b[2]==b[3] or b[4]==b[7] or b[1]==b[4] or b[1]==b[7])
    and (b[1]!=' 'and b[2]!=' 'and b[3]!=' 'and b[4]!=' 'and b[5]!=' 'and b[6]!=' 'and b[7]!=' 'and b[8]!=' 'and b[9]!=' ')):
        game=lose
    else:
        game=0

while(game==0):
    createBoard()
    
    chose = int(input('position: '))
    if(CheckPosition(chose)):
        mark = str(input('number: '))
        b[chose]=mark
        checkWin()
createBoard()
if game==win:
    print("winnnnn")
else:
    print("loseeeee")