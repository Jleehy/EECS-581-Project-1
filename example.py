from board import Board
from interface import Interface

def main():
    player1 = Board() # create a board for player 1
    player2 = Board() # create a board for player 2

    app = Interface(player1, player2) # create a interface object with both players assigned
    
    app.print_board(player1) # print board for player 1

    app.place_ship(player1, "A1", "C1") # place a ship at cell A1 to C1

    app.place_ship(player1, "A3", "A4") # place a ship at cell A1 to C1

    #app.place_ship(player1, "A1", "B2") # debug : place a ship diag at cell A1 to B2

    app.print_board(player1) # print the new contents of the board for player 1

    app.print_board(player1, censored=True) # print a censored version of player 1's board to player 2
 
if __name__ == "__main__":
    main()