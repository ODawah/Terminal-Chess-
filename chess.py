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


def make_move(PLAYER, x1, y1, x2, y2):
    board = new_board()
    if(PLAYER == 1 and board[x1][y1][0]=="W"):
        if(board[x1][y1][1] == "p"):
            if not ( (y2-y1 == 2) or (y2 - y1 == 1)):
                print("pawn doesn't move like that")

    if(PLAYER == 2 and board[x1][y1][0]=="B"):
        if(board[x1][y1][1] == "p"):
            if not ( (y2-y1 == -2) or (y2 - y1 == -1)):
                print("pawn doesn't move like that")

    # moving on board
    board[x1][y1], board[x2][y2] = "-", board[x1][y1]


def draw_board(board):
    pass


def announce_winner(PLAYER):
    pass


def check_winner(BOARD, PLAYER):
    pass
