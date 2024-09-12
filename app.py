import sys

class App:
    def __init__(self, player1, player2, num_ships=0):
        self.config = {0: "□", 1: "■", 2: "•", 3: "○"}  # 0: blank, 1: ship, 2: hit, 3: miss
        self.player1 = player1 # Holds a board object for Player 1.
        self.player2 = player2 # Holds a board object for Player 2.
        self.num_ships = num_ships

    @staticmethod
    # Check if the program should exit.
    def check_quit(action):
        if action[0].upper() == 'Q':
            sys.exit("\nExiting...\n")

    # Prompt the user for a ship coordinate, ensuring a valid input.
    def prompt_ship_coordinate(self, ship_number, part):
        while True:
            coord = input(f"Coordinate for the {part} of ship {ship_number + 1}, with dimensions 1x{ship_number+1}: ").strip().upper()[:3]
            self.check_quit(coord)
            if self._is_valid_coordinate(coord[0], coord[1:]):
                return coord
            
    # Prompt the user for the number of ships to play with, ensuring a valid input.
    def prompt_num_ships(self):
        while True:
            num_ships = input("Enter the number of ships: ")
            self.check_quit(num_ships)
            if num_ships.isnumeric():
                num_ships = int(num_ships)
                if not (num_ships > 0 and num_ships < 6):
                    print("The number of ships must be an integer between 1 and 5.")
                else:
                    self.num_ships = num_ships
                    return
            else:
                print("The number of ships must be an integer between 1 and 5.")
    
    @staticmethod
    # Return whether a ship is placed diagonally or not.
    def is_diagonal(stern_x, bow_x, stern_y, bow_y):
        if stern_x != bow_x and stern_y != bow_y:
            print("Ships must be placed horizontally or vertically\n")
            return True
        
        return False

    @staticmethod
    # Return if the coordinate is valid.
    def _is_valid_coordinate(x, y):
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

    # Place a ship on a player's board and validate placement.
    def place_ship(self, player, stern_x, stern_y, bow_x, bow_y, ship_size):
        if self.is_diagonal(stern_x, bow_x, stern_y, bow_y):
            return False

        # Verify the ship length is correct
        if ((stern_x == bow_x) and (abs(stern_y - bow_y) == ship_size - 1)) or ((stern_y == bow_y) and (abs(stern_x - bow_x) == ship_size - 1)):
            if not player.place_ship(stern_x, stern_y, bow_x, bow_y):
                print("Ships cannot overlap.")
                return False
            return True
        else:
            print(f"The length of ship must be {ship_size}.")
            return False

    # Print a player's board with literal coordinates.
    def print_board(self, player, censored=False):
        column_headers = "\n   " + "   ".join("A B C D E F G H I J".split()) # add column headers (A-J)
        print(column_headers)

        # create the formatted board with row numbers and symbols
        for i, row in enumerate(player.matrix):
            # add row numbers (1-10), then the formatted row contents
            if censored:
                row_str = f"{i+1:2} " + " | ".join(self.config[0] if cell == 1 else self.config[cell] for cell in row)
            else:
                row_str = f"{i+1:2} " + " | ".join(self.config[cell] for cell in row)
            print(row_str)

        print()

