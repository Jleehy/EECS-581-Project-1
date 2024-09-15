from app import App
from board import Board
import cursor

# ANSI Escape Sequences Reference: https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797

def main():
    # Create each player's board.
    name1 = input("Enter the first player's name: ")
    name2 = input("Enter the second player's name: ")
    player1 = Board(name1)
    player2 = Board(name2)
    players = [player1, player2]
    
    # Create the Battleship app.
    app = App(player1, player2)

    # Prompt the user to enter the number of ships to be played.
    app.prompt_num_ships()

    # Give each player a chance to place their ships.
    for player in players:
        cursor.erase()
        action = input(f"\n{player.name}, press Enter to begin placing your ships...")
        app.check_quit(action)

        cursor.move_up(1)
        cursor.erase()

        print(player.name + "'s turn to place their ships")

        # For each ship in the player's arsenal.
        for ship in range(app.num_ships):
            cursor.erase()
            app.print_board(player)

            print("Coordinate input format: A1")
            print("Valid x-coordinates: A - J")
            print("Valid y-coordinates: 1 - 10\n")

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

            # Move the cursor to the line after "Player #'s turn to place their ships".
            cursor.move_to(4)

        cursor.erase()
        app.print_board(player) # Ensure board prints on last turn.

        # Ask the player if they are ready to turn the device over to the second player.
        action = input(f"{player.name}, press Enter after reviewing your ship placements...")
        app.check_quit(action)

        # Move the cursor to the line after "Enter the number of ships" to
        # prepare to clear the screen for Player 2 to place their ships.
        cursor.move_to(2)

    # Begin the game loop.
    current_player = 0
    while True:
        attacker = players[current_player]
        defender = players[abs(current_player - 1)]

        cursor.move_to(0)
        cursor.erase()

        print(attacker.name + "'s turn to attack\n")
        action = input(f"{attacker.name}, press Enter to begin attacking...")
        app.check_quit(action)

        cursor.move_up(1)
        cursor.erase()

        # Print the current player's board
        print("Your Board")
        app.print_board(attacker)

        # Print the enemy's board (the other player's board, censored)
        print("Enemy's Board")
        app.print_board(defender, censored=True)

        while True:
            coord = app.prompt_attack_coordinate()
            if not app.attack(attacker, defender, coord): # Don't allow the attacker to attack the same coordinate twice
                cursor.move_to(31)
                cursor.erase()
                print("You've already attacked that coordinate")
                continue

            break

        # Check if all ships of the enemy have been sunk
        if defender.all_ships_sunk():
            print(f"\n{attacker.name} wins! All of {defender.name}'s ships have been sunk!\n")
            break  # Exit the game loop to end the game

        # Ask the player if they are ready to turn the device over to the second player.
        action = input(f"\n{attacker.name}, press Enter when you're done reviewing your attacks...")
        app.check_quit(action)

        # Switch to the other player
        current_player = abs(current_player - 1)

if __name__ == "__main__":
    main()
