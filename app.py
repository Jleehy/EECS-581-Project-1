class App:
    def __init__(self, player1, player2, num_ships):
        self.config = {0: "□", 1: "■", 2: "•", 3: "○"}  # 0: blank, 1: ship, 2: hit, 3: miss
        self.player1 = player1 # Holds a board object for Player 1.
        self.player2 = player2 # Holds a board object for Player 2.
        # Todo: Add current_player
        
        # NOTE: Currently unused logic. Neccessary for main game loop.
        self.num_ships = num_ships

    # Attack a cell on a player's board given literal coordinates.
    def attack(self, attacker, defender, pos):
        # Cast the input initially for easier error checking
        col, row = ord(pos[0]), int(pos[1:])

        col_index, row_index = self._is_valid_coordinate(col, row) # Convert literal to an index.

        defender.attack(col_index, row_index) # Attack player's board on the indices.

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

