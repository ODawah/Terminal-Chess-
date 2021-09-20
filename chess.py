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


def make_move(PLAYER, x_to_move, y_to_move, x_move_to, y_move_to):
    board = new_board()
    if(PLAYER == 1 and board[x_to_move][y_to_move][0]=="W"):
        pass

    if(PLAYER == 2 and board[x_to_move][y_to_move][0]=="B"):
        pass


    board[x_to_move][y_to_move], board[x_move_to][y_move_to] = "-", board[x_to_move][y_to_move]


def draw_board(board):
    pass


def announce_winner(PLAYER):
    pass


def check_winner(BOARD, PLAYER):
    pass
