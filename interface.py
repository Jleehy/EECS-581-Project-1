class Interface:
    def __init__(self, player1, player2):
        self.config = {0: "□", 1: "■", 2: "•", 3: "○"}  # 0: blank, 1: ship, 2: hit, 3: miss
        self.player1 = player1 # holds a board object for player 1
        self.player2 = player2 # holds a board object for player 2

    def place_ship(self, player, start_pos, end_pos):
        # still missing error checks and other logic such as what happens if 1A is passed instead of A1, etc...        

        # Cast the input initially for easier error checking
        start_col, start_row = ord(start_pos[0]), int(start_pos[1:])
        end_col, end_row = ord(end_pos[0]), int(end_pos[1:]) 

        
        ''' for debugging
        print(type(start_col), " ", type(start_row))
        print(start_col, " ", start_row)
        '''

        # Check that the column is A-J and row is 1-10
        if not(65 <= start_col <= 74):
            print("Start column out of range\n")
        elif not(1 <= start_row <= 10):
            print("Start row out of range\n")
        else:
            print("Start column and row in range\n")

        if not(65 <= end_col <= 74):
            print("End column out of range\n")
        elif not(1 <= end_row <= 10):
            print("End row out of range\n")
        else:
            print("End column and row in range\n")
        

        # convert columns A-J to indices 0-9
        start_col_index = start_col - ord("A")
        end_col_index = end_col - ord("A")

        # convert rows (1-10) to indices (0-9)
        start_row_index = int(start_row) - 1
        end_row_index = int(end_row) - 1

        player._place_ship(start_row_index, start_col_index, end_row_index, end_col_index)

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
