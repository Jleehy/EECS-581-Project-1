from app import App
from board import Board

def main():
    # Create each player's board
    player1 = Board()
    player2 = Board()

    # Note: num_ships is currently unused
    # Create the Battleship app
    app = App(player1, player2, num_ships = 2)

    while (True):
        app.print_board(player1)

        action = input("Enter your action: ")
        if (action.lower() == "q"):
            break


if __name__ == "__main__":
    main()