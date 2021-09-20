from chess import new_board,draw_board, make_move,check_winner,announce_winner



PLAYER_1 = 1
PLAYER_2 = 2
board = new_board()


if __name__ == "__main__":
    while True:
        draw_board(board)
        make_move(PLAYER_1)
        if check_winner(board, PLAYER_1):
            announce_winner(PLAYER_1)
            break
        draw_board(board)
        make_move(PLAYER_2)
        if check_winner(board, PLAYER_2):
            announce_winner(PLAYER_1)
            break