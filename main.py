from chess import new_board,draw_board, make_move,check_winner,announce_winner



PLAYER_1 = 1
PLAYER_2 = 2
board = new_board()




if __name__ == "__main__":
    while True:
        draw_board(board)

        print("enter x1 position")
        x1 = int(input())
        print("enter y1 position")
        y1 = int(input())
        print("enter x2 position")
        x2 = int(input())
        print("enter y2 position")
        y2 = int(input())

        make_move(PLAYER_1,x1,y1,x2,y2)
        if check_winner(board, PLAYER_1):
            announce_winner(PLAYER_1)
            break
        draw_board(board)
        make_move(PLAYER_2,x1,y1,x2,y2)
        if check_winner(board, PLAYER_2):
            announce_winner(PLAYER_1)
            break