class Interface:
    def __init__(self, player1, player2):
        self.config = {0: "□", 1: "■", 2: "•", 3: "○"}  # 0: blank, 1: ship, 2: hit, 3: miss
        self.player1 = player1 # holds a board object for player 1
        self.player2 = player2 # holds a board object for player 2

    def place_ship(self, player, position):
        # still missing error checks and other logic such as what happens if 1A is passed instead of A1, etc...
        col, row = position[0], position[1:] 
        col_to_index = ord(col) - ord("A")
        row_to_index = int(row) - 1
        player._place_ship(col_to_index, row_to_index)

    def print_board(self, player, censored=False):
        column_headers = "   " + "   ".join("A B C D E F G H I J".split()) # add column headers (A-J)
        print(column_headers)

        # create the formatted board with row numbers and symbols
        for i, row in enumerate(player.matrix):
            # add row numbers (1-10), then the formatted row contents
            if censored:
                row_str = f"{i+1:2} " + " | ".join(self.config[0] if cell == 1 else self.config[cell] for cell in row)
            else:
                row_str = f"{i+1:2} " + " | ".join(self.config[cell] for cell in row)
            print(row_str)
