def new_board():
    return [
        ["Wr", "Wb", "Wn", "Wq", "Wk", "Wn", "Wb", "Wr"],
        ["Wp", "Wp", "Wp", "Wp", "Wp", "Wp", "Wp", "Wp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["Bp", "Bp", "Bp", "Bp", "Bp", "Bp", "Bp", "Bp"],
        ["Br", "Bb", "Bn", "Bq", "Bk", "Bn", "Bb", "Br"],
    ]


class Pieces:
    def __init__(self, x1, y1, board):
        self.x1 = x1
        self.y1 = y1
        self.current = board[x1][y1]

    def validMove(self, x2, y2):
        pass


class Pawn:
    def __init__(self, x2, y2):
        self.x2 = x2
        self.y2 = y2

    def rule(self,player,x1,y1):
        if player == 1:
            if (y2 - y1 == 2) and x1 == 1:
                return True
            elif (y2 - y1 == 1:
                return True
            else:
                print("pawn doesn't move like that")
                return False

        elif player == 2:
            if (y2 - y1 == -2) and x1 == 6:
                return True
            elif (y2 - y1 == -1):
                return True
            else:
                print("pawn doesn't move like that")
                return False


class Rook:
    def __init__(self, x2, y2):
        self.x2 = x2
        self.y2 = y2

    def rule(self, x1, y1):
        if  (abs(self.x2 - x1) == 0) or (abs(self.y2 - y1) == 0):
            return True
        else:
            return False


class Knight:
    def __init__(self, x2, y2):
        self.x2 = x2
        self.y2 = y2

    def rule(self, x1, y1):
        if (abs(self.y2 - y1) == 2 and abs(self.x2 - x1) == 1) or (abs(self.y2 - y1) == 1 and abs(self.x2 - x1) == 2):
            return True
        else:
            return False
            


class Bishop:
    def __init__(self, x2, y2):
        self.x2 = x2
        self.y2 = y2

    def rule(self, x1, y1):
        if abs((x1 - self.x2) / (y1 - self.y2)):
            return True
        else:
            return False


class Queen:
    def __init__(self, x2, y2):
        self.x2 = x2
        self.y2 = y2

    def rule(self, x1, y1):
        if (
            (abs((x1 - self.x2) / (y1 - self.y2)) == 1)
            or ((x1 - self.x2) == 0)
            or ((y1 - self.y2) == 0)
        ):
            return True
        else:
            return False


class king:
    def __init__(self, x2, y2):
        self.x2 = x2
        self.y2 = y2

    def rule(self, x1, y1):
        if (self.x2 - x1 > 1) or (self.y2 - y1 > 1):
            return True
        else:
            return False


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
        for i in range(0, 9):
            if BOARD[i].index("Bk"):
                return announce_winner(PLAYER)
    else:
        for i in range(0, 9):
            if BOARD[i].index("Wk"):
                return announce_winner(PLAYER)
