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

                # Place the player's ship on their board.
                if app.place_ship(player, stern, bow, ship + 1):
                    break

        app.print_board(player) # Ensure board prints on last turn.

        # Ask the player if they are ready to turn the device over to the second player.
        action = input(f"{player.name}, are you ready to turn the device over to the next player? Press Enter to continue...")
        app.check_quit(action)
        # NOTE : MISSING TERMINAL CLEAR LOGIC

    # Begin the game loop.
    while True:
        # NOTE: Generic prints for now. I just want to debug attack. Currently using player1 and player2 instead of a variable that grabs current player.
        # this isnt a game loop yet its just for debug purposes.

        print("Player 1's turn")
        print("Your Board")
        app.print_board(player1)
        print("Enemies Board")
        app.print_board(player2, censored=True)

        pos = app.prompt_attack_coordinate()
        hit, sink = app.attack(player2, pos)

        if not hit:
            print("MISSED!")
        if hit:
            print(f"HIT PLAYER 2 @ {pos}")
        if sink:
            print("SUNK PLAYERS SHIP OF SIZE X")
        break

if __name__ == "__main__":
    main()
