import numpy
board=numpy.array([['_','_','_'],['_','_','_'],['_','_','_']])
p1s='X'
p2s='O'
def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,'Won')
    return False

def check_cols(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,'Won')
    return False

def check_diagnols(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        print(symbol,"Won")
        return True
    
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
        print(symbol,"Won")
        return True
    return False

def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagnols(symbol)

def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input("Enter Row-1 or 2 or 3="))#Alt+Shift+DownArrow
        col=int(input("Enter Column-1 or 2 or 3="))

        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=="_":
            break
        else:
            print("Invalid Input. Please Enter Again!!!")
    board[row-1][col-1]=symbol

def play():
    for turn in range(9):
        if turn%2==0:
            print('Xs Turn')
            place(p1s)
            if won(p1s):
                break
        else:
            print('Os Turn')
            place(p2s)
            if won(p2s):
                break
    if not(won(p1s)) and not(won(p2s)):
         print("Draw")
play()
