from app import App
from board import Board


def main():
    # Create each player's board.
    player1 = Board("Player 1")
    player2 = Board("Player 2")
    
    # Create the Battleship app.
    app = App(player1, player2)

    # Prompt the user to enter the number of ships to be played.
    app.prompt_num_ships()

    # Give each player a chance to place their ships.
    for player in [player1, player2]:
        print(player.name + "'s turn to place their ships")

        # For each ship in the player's arsenal.
        for ship in range(app.num_ships):
            app.print_board(player)

            while True:
                # If the ship size is 1, assign both bow and stern to the same coordinate.
                if ship == 0:
                    stern = bow = app.prompt_ship_coordinate(ship, "rear")
                else:
                    stern = app.prompt_ship_coordinate(ship, "rear") # Rear coordinate of the ship.
                    bow = app.prompt_ship_coordinate(ship, "front") # Front coordinate of the ship.

                # Create indices for the stern and bow.
                # Note: There is no need to wrap this in a try-except because
                # is_valid_coordinate ensures stern[1:] and bow[1:] can be cast
                # to integers.
                stern_x = int(stern[1:]) - 1
                stern_y = ord(stern[0]) - ord('A')
                bow_x = int(bow[1:]) - 1
                bow_y = ord(bow[0]) - ord('A')

                # Place the player's ship on their board.
                if app.place_ship(player, stern_x, stern_y, bow_x, bow_y, ship + 1):
                    break

        app.print_board(player) # Ensure board prints on last turn.

        # Ask the player if they are ready to turn the device over to the second player.
        input(f"{player.name}, are you ready to turn the device over to the next player? Press Enter to continue...")
        app.check_quit(action)
        # NOTE : MISSING TERMINAL CLEAR LOGIC

    # Begin the game loop.
    while True:
        app.print_board(player1)

        action = input("Enter your action: ")
        app.check_quit(action)

if __name__ == "__main__":
    main()
