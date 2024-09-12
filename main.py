import sys

from app import App
from board import Board

# Check if the program should exit.
def check_quit(action):
    if action[0].upper() == 'Q':
        sys.exit("\nExiting...\n")

# Prompt the user for the number of ships to play with, ensuring a valid input.
def prompt_ships():
    while True:
        num_ships = input("Enter the number of ships: ")
        check_quit(num_ships)
        if num_ships.isnumeric():
            num_ships = int(num_ships)
            if not (num_ships > 0 and num_ships < 6):
                print("The number of ships must be an integer between 1 and 5.")
            else:
                return num_ships
        else:
            print("The number of ships must be an integer between 1 and 5.")

# Prompt the user for a ship coordinate, ensuring a valid input.
def prompt_ship_coordinate(ship_number, part, player):
    while True:
        coord = input(f"Coordinate for the {part} of ship {ship_number + 1}, with dimensions 1x{ship_number+1}: ").strip().upper()[:3]
        check_quit(coord)
        if player.is_valid_coordinate(coord[0], coord[1:]):
            return coord
        
def is_diagonal(stern_x, bow_x, stern_y, bow_y):
    if stern_x != bow_x and stern_y != bow_y:
       print("Ships must be placed horizontally or vertically\n")
       return True
    
    return False

def main():
    # Create each player's board.
    player1 = Board("Player 1")
    player2 = Board("Player 2")

    num_ships = prompt_ships() 
    
    # Create the Battleship app.
    app = App(player1, player2, num_ships)

    # Give each player a chance to place their ships.
    for player in [player1, player2]:
        print(player.name + "'s turn to place their ships")

        # For each ship in the player's arsenal.
        for ship in range(app.num_ships):
            app.print_board(player)

            while True:
                # If the ship size is 1, assign both bow and stern to the same coordinate.
                if ship == 0:
                    stern = bow = prompt_ship_coordinate(ship, "rear", player)
                else:
                    stern = prompt_ship_coordinate(ship, "rear", player) # Rear coordinate of the ship.
                    bow = prompt_ship_coordinate(ship, "front", player) # Front coordinate of the ship.

                # Create indices for the stern and bow.
                # Note: There is no need to wrap this in a try-except because
                # is_valid_coordinate ensures stern[1:] and bow[1:] can be cast
                # to integers.
                stern_x = int(stern[1:]) - 1
                stern_y = ord(stern[0]) - ord('A')
                bow_x = int(bow[1:]) - 1
                bow_y = ord(bow[0]) - ord('A')

                # Don't allow diagonal placement of ships.
                if is_diagonal(stern_x, bow_x, stern_y, bow_y):
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
