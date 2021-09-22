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

class pieces():

    def __init__(self,x1,y1,board):
        self.x1 = x1
        self.y1 = y1
        self.current = board[x1][y1]

    def current_position(self): 
        return self.x1,self.y1

    def validMove(self,x2,y2):
        pass




def pawn(player, x1, x2, y1, y2, board):
    if player == 1:
        if (y2 - y1 == 2) and (board[x2][y2] == "-") and x1 == 1:
            return True
        elif (y2 - y1 == 1) and board[x2][y2] == "-":
            return True
        else:
            print("pawn doesn't move like that")
            return False

    elif player == 2:
        if (y2 - y1 == -2) and board[x2][y2] == "-" and x1 == 6:
            return True
        elif (y2 - y1 == -1) and board[x2][y2] == "-":
            return True
        else:
            print("pawn doesn't move like that")
            return False


def rook(x1, x2, y1, y2, board):
    for x in range(x1, x2):
        if board[x][y2] != "-":
            print("rook doesn't move like that")
            return False
    if board[x1][y1][0] != board[x2][y2][0] :
        return True
    


def knight(x1, x2, y1, y2, board):
    if ((x2 - x1 == (2 or -2)) and (y2 - y1 == (1 or -1))) or (
        (y2 - y1 == (2 or -2))
        and (x2 - x1 == (1 or -1))
        and board[x2][y2][0] != board[x1][x2][0]):
        return True
    else:
        return False

def bishop(x1,x2,y1,y2,board):
    for i ,j in range(x2,y2):
        if(i-j != 0 and board[i][j] != "-"):
            return False
    if (board[x2][y2][0] != board[x1][x2][0]):
            return True

def queen(x1,x2,y1,y2,board):
    for i ,j in range(x2,y2):
        if ((i-j != 0 and board[i][j] != "-") or (board[i][j] != "-") ):
            return False
    if (board[x2][y2][0] != board[x1][x2][0]):
            return True

class king:
    def __init__(self,x2,y2,current):
        self.x2 = x2
        self.y2 = y2
        pieces.current_position = current 

    def rule(self):
        if (current.x1 - self.x2 > 1) or (current.y1 - self.y2 > 1): 
            pass

    
    

            


def make_move(PLAYER, x1, y1, x2, y2):
    board = new_board()

    if PLAYER == 1 and board[x1][y1][0] == "W":
        if board[x1][y1][1] == "p":
            if pawn(PLAYER, x1, x2, y1, y2, board):
                board[x1][y1], board[x2][y2] = "-", board[x1][y1]
                draw_board(board)
        elif board[x1][y1] == "r":
                if rook(x1, x2, y1, y2, board):
                    board[x1][y1], board[x2][y2] = "-", board[x1][y1]
                    draw_board(board)
        elif board[x1][y1] == "b":
                if bishop(x1, x2, y1, y2, board):
                    board[x1][y1], board[x2][y2] = "-", board[x1][y1]
                    draw_board(board)
        elif board[x1][y1] == "n":
                if knight(x1, x2, y1, y2, board):
                    board[x1][y1], board[x2][y2] = "-", board[x1][y1]
                    draw_board(board)
        elif board[x1][y1] == "q":
                if queen(x1, x2, y1, y2, board):
                    board[x1][y1], board[x2][y2] = "-", board[x1][y1]
                    draw_board(board)
        
    if PLAYER == 2 and board[x1][y1][0] == "B":
        if board[x1][y1][1] == "p":
            if pawn(PLAYER, x1, x2, y1, y2, board):
                board[x1][y1], board[x2][y2] = "-", board[x1][y1]
                draw_board(board)
        elif board[x1][y1] == "r":
                if rook(x1, x2, y1, y2, board):
                    board[x1][y1], board[x2][y2] = "-", board[x1][y1]
                    draw_board(board)
        elif board[x1][y1] == "b":
                if bishop(x1, x2, y1, y2, board):
                    board[x1][y1], board[x2][y2] = "-", board[x1][y1]
                    draw_board(board)
        elif board[x1][y1] == "n":
                if knight(x1, x2, y1, y2, board):
                    board[x1][y1], board[x2][y2] = "-", board[x1][y1]
                    draw_board(board)
        elif board[x1][y1] == "q":
                if queen(x1, x2, y1, y2, board):
                    board[x1][y1], board[x2][y2] = "-", board[x1][y1]
                    draw_board(board)
                else:
                    print("Play with your pieces only")


def draw_board(board):
        print(*board, sep="\n")


def announce_winner(PLAYER):
    if PLAYER == 1:
        print("PLAYER ONE WINS!!")
        return PLAYER
    else:
        print("PLAYER TWO WINS!!")

def check_winner(BOARD, PLAYER):
    if PLAYER == 1:
        for i in range (0,9):
            if BOARD[i].index("Bk"):
                return announce_winner(PLAYER)
    else:
        for i in range (0,9):
            if BOARD[i].index("Wk"):
                return announce_winner(PLAYER)
