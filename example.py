from board import Board
from app import App

def main():
    player1 = Board() # Create a board object for Player 1.
    player2 = Board() # Create a board object for Player 2.

    #NOTE: num_ships is currently unused
    app = App(player1, player2, num_ships=2) # Create an app object containing both players and the number of ships.
    
    print("PRINTING PLAYER 1 BOARD") # DEBUG PURPOSES
    app.print_board(player1) # Print Player 1's board.
    print("PLACED SHIP AT A1:C1 (0,0:0,2)") # DEBUG PURPOSES
    app.place_ship(player1, "A1", "C1") # Place a ship at cell A1 to C1 on Player 1's board. (Should be horizontal)
    print("PRINTING PLAYER 1 BOARD") # DEBUG PURPOSES
    app.print_board(player1) # Print the new contents of Player 1's board.
    print("PLACED SHIP AT A3:C4 (2,0:3,0)") # DEBUG PURPOSES
    app.place_ship(player1, "A3", "A4") # Place a ship at cell A3 to A4 on Player 1's board. (Should be vertical)

    #app.place_ship(player1, "A1", "B2") # DEBUG : # Place a ship at cell A1 to B2 on Player 1's board. (Should be invalid)

    print("PRINTING PLAYER 1 BOARD") # DEBUG PURPOSES
    app.print_board(player1) # Print the new contents of Player 1's board.
    print("PLAYER 2 ATTACKS PLAYER 1 BOARD AT A1 (0,0)")
    app.attack(player2, player1, "A1") # Player 2 attacks Player 1's board at A1

    print("PLAYER 2 ATTACKS PLAYER 1 BOARD AT I0 (0,8)") # DEBUG PURPOSES
    app.attack(player2, player1, "I1") # Player 2 attacks Player 1's board at I1

    print("PRINTING CENSORED PLAYER 1 BOARD") # DEBUG PURPOSES
    app.print_board(player1, censored=True) # Print a censored version of Player 1's board to Player 2
 
if __name__ == "__main__":
    main()