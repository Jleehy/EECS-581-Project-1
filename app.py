import sys

class App:
    def __init__(self, player1, player2, num_ships=0):
        # 0: blank, 1 - 5: ships of different colors, 6: red hit, 7: white miss
        # 1: blue
        # 2: green
        # 3: yellow
        # 4: light purple
        # 5: cyan
        self.config = {0: "□", 1: "\033[34m■\033[0m", 2: "\033[32m■\033[0m", 3: "\033[33m■\033[0m", 4: "\033[35m■\033[0m", 5: "\033[36m■\033[0m", 6: "\033[31m•\033[0m", 7: "■"} 
        self.player1 = player1 # Holds a board object for Player 1.
        self.player2 = player2 # Holds a board object for Player 2.
        self.num_ships = num_ships

    # Place a ship on a player's board and validate placement. 
    # Returns False if ship placement is unsuccessful and true if it is
    def place_ship(self, player, stern, bow, ship_size):
        # Create indices for the stern and bow.
        # Note: There is no need to wrap this in a try-except because
        # is_valid_coordinate ensures stern[1:] and bow[1:] can be cast
        # to integers.
        stern_row, stern_col, bow_row, bow_col = self.literals_to_indices(stern, bow)
        return player.place_ship(stern_row, stern_col, bow_row, bow_col, ship_size) # player.place_ship checks for validity
    
    # Attack a cell on a player's board.
    def attack(self, attacker, defender, pos):
        """
        #NOT UPDATED THIS WAS FOR DEBUG.PY
        # Cast the input initially for easier error checking
        x, y = self.literals_to_indices(pos)

        defender.attack(x, y) # Attack player's board on the indices.
        """
        
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

    @staticmethod
    # Convert literal coordinates to indices.
    def literals_to_indices(stern, bow=None):
        stern_row = int(stern[1:]) - 1
        stern_col = ord(stern[0]) - ord('A')
        if bow == None:
            return stern_row, stern_col
        else:
            bow_row = int(bow[1:]) - 1
            bow_col = ord(bow[0]) - ord('A')
            return stern_row, stern_col, bow_row, bow_col

    @staticmethod
    # Check if the program should exit.
    def check_quit(action):
        if len(action) == 0:
            return
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
