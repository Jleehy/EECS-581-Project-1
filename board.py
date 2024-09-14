from ship import Ship

class Board:

    def __init__(self, name):
        self.name = name
        self.matrix = [[0] * 10 for _ in range(10)] # Initialize a 10x10 matrix with zeroes.
        self.ships = [] # Store ships placed on the board.

    # Place a ship on board given indices. returns true if placed successfully, false if not.
    def place_ship(self, stern_row, stern_col, bow_row, bow_col, correct_length):
        
        # Check if the ship is being placed diagonally.
        if self.is_diagonal(stern_row, stern_col, bow_row, bow_col):
            return False

        # Check if the ship is the correct length.
        if not self.is_correct_length(stern_row, stern_col, bow_row, bow_col, correct_length):
            return False
        
        vert_bool = (stern_row == bow_row) # Determine if the ship is vertical or not.
        if stern_row > bow_row or stern_col > bow_col: #fixes overlap issue
            stern_row, bow_row = bow_row, stern_row
            stern_col, bow_col = bow_col, stern_col
        new_ship = Ship(correct_length, stern_row, stern_col, vert=vert_bool) # Create a new ship.

        # Check if the ship overlaps with other ships.
        if self.is_overlapping(new_ship):
            return False
            
        self.ships.append(new_ship) # Put the ship in the ship array.

        if vert_bool: # If the ship is vertical, we update the board vertically to include the ship.
            for col in range(min(stern_col, bow_col), max(stern_col, bow_col) + 1):
                self._update_matrix(stern_row, col, correct_length)
        else: # If the ship is vertical, we update the board vertically to include the ship.
            for row in range(min(stern_row, bow_row), max(stern_row, bow_row) + 1):
                self._update_matrix(row, stern_col, correct_length)

        return True # Returns true only if ship was successfully placed.
    
    # Attack player's board, return hit status.
    def attack(self, row, col):
        hit = False  # Flag to track if a hit occurs.
        sunk = False # Flag to track if a sink occurs.
        print(row, col)
        # Iterate through every stored ship
        for ship in self.ships:
            print(ship.indices)
            # Check if the (row, col) match any of the ship's indices
            if (row, col) in ship.indices:
                ship.indices.remove((row, col))  # Remove the hit index from the ship
                hit = True  # Set flag to True if a hit occurs
                self._update_matrix(row, col, 6) # Indicate hit status, red.
                if not ship.indices:
                    sunk = True # Set flag to True if a sink occurs.
                break
        
        return hit, sunk
    
    # Checks if the ships overlap.
    def is_overlapping(self, new_ship):
        for ship in self.ships: # This loop checks if the new ship overlaps with any previous ship, returns false if yes.
            if new_ship._is_overlapping(ship):
                print("Ships cannot overlap.")
                return True

    @staticmethod
    # Checks if the ship is the correct length.
    def is_correct_length(stern_row, stern_col, bow_row, bow_col, correct_length):
        length = max(abs(stern_row - bow_row), abs(stern_col - bow_col)) + 1 # Calculate the length.
        if length != correct_length: # If the length isn't the intended length, tell user and return false.
            print(f"The length of ship must be {correct_length}.")
            return False
        return True

    @staticmethod
    # Checks if the ship is diagonal, returns true if it is.
    def is_diagonal(stern_row, stern_col, bow_row, bow_col):
        if stern_row != bow_row and stern_col != bow_col:
            print("Ships must be placed horizontally or vertically\n")
            return True
        return False

    # Could be overkill but maybe we want future logic.
    def _update_matrix(self, row, col, val):
        self.matrix[row][col] = val

    def all_ships_sunk(self):
        # If all ships have no remaining coordinates (i.e., no part of the ship is still on the board), return True
        return all(len(ship.indices) == 0 for ship in self.ships)
        
    def __repr__(self):
        return f"{self.matrix}"
