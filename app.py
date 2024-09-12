class App:
    def __init__(self, player1, player2, num_ships):
        self.config = {0: "□", 1: "■", 2: "•", 3: "○"}  # 0: blank, 1: ship, 2: hit, 3: miss
        self.player1 = player1 # Holds a board object for Player 1.
        self.player2 = player2 # Holds a board object for Player 2.
        # Todo: Add current_player
        
        # NOTE: Currently unused logic. Neccessary for main game loop.
        if not(1 <= num_ships <=5):
            raise ValueError("Invalid number of ships\n")
        else:
            self.num_ships = num_ships

    # Place a ship on a player's board given literal coordinates. 
    def place_ship(self, player, start_pos, end_pos):
        # Cast the input initially for easier error checking
        start_col, start_row = ord(start_pos[0]), int(start_pos[1:])
        end_col, end_row = ord(end_pos[0]), int(end_pos[1:]) 

        start_col_index, start_row_index = self._is_valid_coordinate(start_col, start_row) # Convert literal to an index.
        end_col_index, end_row_index = self._is_valid_coordinate(end_col, end_row) # Convert literal to an index.

        player.place_ship(start_row_index, start_col_index, end_row_index, end_col_index) # Place a ship on player's board on the indices.

    # Attack a cell on a player's board given literal coordinates.
    def attack(self, attacker, defender, pos):
        # Cast the input initially for easier error checking
        col, row = ord(pos[0]), int(pos[1:])

        col_index, row_index = self._is_valid_coordinate(col, row) # Convert literal to an index.

        defender.attack(col_index, row_index) # Attack player's board on the indices.

    # Check if a coordinate is valid, if so convert literal to indices and return indices.
    def _is_valid_coordinate(self, x, y):
        # Check that the column is in the ranges A-J(65 - 74) and row is 1-10
        if not(65 <= x <= 74) or not(1 <= y <= 10):
            raise ValueError("Invalid start position\n")
        else:
            #print("Start column and row in range\n")
            start_col_index = x - ord("A")
            start_row_index = int(y) - 1

            return start_col_index, start_row_index

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
