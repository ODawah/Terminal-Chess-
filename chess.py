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


def pawn(player, x1, x2, y1, y2, board):
    if player == 1:
        if (y2 - y1 == 2) and (board[x2][y2] == "-") and x1 == 2:
            return True
        elif (y2 - y1 == 1) and board[x2][y2] == "-":
            return True
        else:
            print("pawn doesn't move like that")
            return False

    elif player == 2:
        if (y2 - y1 == -2) and board[x2][y2] == "-" and x1 == 7:
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

def king (x1,x2,y1,y2,board):
    if ( x2-x1 != (1 or -1) or y2-y1 != (1 or -1) or x2-x1 != y2-y1 ):
        return False
    else:
        return True
            


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
        elif board[x1][y1] == "k":
                if king(x1, x2, y1, y2, board):
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
        elif board[x1][y1] == "k":
                if king(x1, x2, y1, y2, board):
                    board[x1][y1], board[x2][y2] = "-", board[x1][y1]
                    draw_board(board)
    else:
        print("Play with your pieces only")


def draw_board(board):
    print(board)


def announce_winner(PLAYER):
    if PLAYER == 1:
        print("PLAYER ONE WINS!!")
    else:
        print("PLAYER TWO WINS!!")

def check_winner(BOARD, PLAYER):
    if PLAYER == 1:
        for i in range (BOARD):
            if BOARD[i].index("Bk") == -1:
                return announce_winner(PLAYER)
    else:
        for i in range (0,9):
            if BOARD[i].index("Wk") == -1:
                return announce_winner(PLAYER)
