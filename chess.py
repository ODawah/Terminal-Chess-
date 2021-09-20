def new_board():
    return [
        ["Wr", "Wb", "Wn", "Wq", "Wk", "Wn", "Wb", "Wr"],
        ["Wp", "Wp", "Wp", "Wp", "Wp", "Wp", "Wp", "Wp"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["Bp", "Bp", "Bp", "Bp", "Bp", "Bp", "Bp", "Bp"],
        ["Br", "Bb", "Bn", "Bq", "Bk", "Bn", "Bb", "Br"],
    ]

def pawn(player,x1,x2,y1,y2,board):
    if(player == 1):
        if ((y2-y1 == 2) and board[x2][y2] == "-":
            return True
        elif( (y2 - y1 == 1) and board[x2][y2] == "-"):
            return True
        else: 
             print("pawn doesn't move like that")
            return False

    elif (player == 2):
       if ((y2-y1 == -2) and board[x2][y2] == "-":
            return True
        elif( (y2 - y1 == -1) and board[x2][y2] == "-"):
            return True
        else: 
             print("pawn doesn't move like that")
            return False

def rook(x1,x2,y1,y2,board):
        for x in range (x1,x2):
            if board[x][y2] != "-":
                print("rook doesn't move like that")
                return False
            else:
                return True






def make_move(PLAYER, x1, y1, x2, y2):
    board = new_board()
    if(PLAYER == 1 and board[x1][y1][0]=="W"):
        if(board[x1][y1][1] == "p"):
            if (pawn(PLAYER,x1,x2,y1,y2,board)):
                board[x1][y1], board[x2][y2] = "-", board[x1][y1]
            
            elif(board[x1][y1] == "r"):
                if(rook(PLAYER,x1,x2,y1,y2,board)):
                board[x1][y1], board[x2][y2] = "-", board[x1][y1]
                

    if(PLAYER == 2 and board[x1][y1][0]=="B"):
        if(board[x1][y1][1] == "p"):
            if (pawn(PLAYER,x1,x2,y1,y2,board)):
                board[x1][y1], board[x2][y2] = "-", board[x1][y1]
        elif(board[x1][y1] == "r"):
            if(rook(PLAYER,x1,x2,y1,y2,board)):
                board[x1][y1], board[x2][y2] = "-", board[x1][y1]
    else:
        print('Play with your pieces only')

    


def draw_board(board):
    pass


def announce_winner(PLAYER):
    pass


def check_winner(BOARD, PLAYER):
    pass
