import sys

from app import App
from board import Board

# Check if the program should exit.
def check_quit(action):
    if action[0].upper() == 'Q':
        sys.exit("\nExiting...\n")

# Return if the coordinate is valid.
def is_valid_coordinate(x, y):
    # Valid x-coordinates: A - J.
    if x < 'A' or x > 'J':
        print("X-coordinate must be in the range A - J\n")
        return False

    # Protect against ValueErrors since y may not be an int.
    try:
        # Valid y-coordinates: 1 - 10.
        if int(y) < 1 or int(y) > 10:
            print("Y-coordinate must be in the range 1 - 10\n")
            return False
    except ValueError as e:
        print("Y-coordinate must be an integer in the range 1 - 10\n")
        return False



    return True

def main():
    # Create each player's board.
    player1 = Board("Player 1")
    player2 = Board("Player 2")

    ships_okay = True
    num_ships = 0
    while ships_okay:
        num_ships = input("Enter the number of ships: ")
        if num_ships.isnumeric():
            num_ships = int(num_ships)
            if not (num_ships > 0 and num_ships < 6):
                print("The number of ships must be an integer between 1 and 5.")
            else:
                ships_okay = False
        else:
            print("The number of ships must be an integer between 1 and 5.")


        # Note: num_ships is currently unused.
        # Create the Battleship app.
        app = App(player1, player2, num_ships)

    # Give each player a chance to place their ships.
    for player in [player1, player2]:
        print(player.name + "'s turn to place their ships\n")

        # For each ship in the player's arsenal.
        for ship in range(app.num_ships):
            app.print_board(player)

            while True:
                stern = ""
                bow = ""

                # Get the coordinate for the stern (rear) of the ship.
                while True:
                    stern = input(f"Coordinate for the rear of ship {ship + 1}, with dimensions 1x{ship+1}: ").strip().upper()[:3]
                    check_quit(stern)
                    if is_valid_coordinate(stern[0], stern[1:]):
                        break

                # Get the coordinate for the bow (front) of the ship.
                while True:
                    bow = input(f"Coordinate for the front of ship {ship + 1}: ").strip().upper()[:3]
                    check_quit(bow)
                    if is_valid_coordinate(bow[0], bow[1:]):
                        break

                # Create indices for the stern and bow.
                # Note: There is no need to wrap this in a try-except because
                # is_valid_coordinate ensures stern[1:] and bow[1:] can be cast
                # to integers.
                stern_x = int(stern[1:]) - 1
                stern_y = ord(stern[0]) - ord('A')
                bow_x = int(bow[1:]) - 1
                bow_y = ord(bow[0]) - ord('A')

                # Don't allow diagonal placement of ships.
                if stern_x != bow_x and stern_y != bow_y:
                    print("Ships must be placed horizontally or vertically\n")
                    continue

                # Place the player's ship on their board.
                # Verifies that the ship length is correct
                if ((stern_x == bow_x) and (abs(stern_y - bow_y) == (ship))) or ((stern_y == bow_y) and (abs(stern_x - bow_x) == (ship))):
                    if not player.place_ship(stern_x, stern_y, bow_x, bow_y):
                        print("Ships cannot overlap.")
                        continue
                else:
                    print(f"The length of ship {ship+1} must be {ship+1}.")
                    continue
                break

    # Begin the game loop.
    while True:
        app.print_board(player1)

        action = input("Enter your action: ")
        check_quit(action)




if __name__ == "__main__":
    main()
