from ship import Ship

class Board:

    def __init__(self, name):
        self.name = name
        self.matrix = [[0] * 10 for _ in range(10)] # Initialize a 10x10 matrix with zeroes.
        self.ships = [] # Store ships placed on the board.

    # Place a ship on board given indices. returns true if placed successfully, false if not.
    def place_ship(self, stern_x, stern_y, bow_x, bow_y, correct_length):
        
        # Check if the ship is being placed diagonally.
        if self.is_diagonal(stern_x, stern_y, bow_x, bow_y):
            return False

        # Check if the ship is the correct length.
        if not self.is_correct_length(stern_x, stern_y, bow_x, bow_y, correct_length):
            return False
        
        vert_bool = (stern_x == bow_x) # Determine if the ship is vertical or not.
        new_ship = Ship(correct_length, stern_x, stern_y, vert=vert_bool) # Create a new ship.

        # Check if the ship overlaps with other ships.
        if self.is_overlapping(new_ship):
            return False
            
        self.ships.append(new_ship) # Put the ship in the ship array.

        if vert_bool: # If the ship is vertical, we update the board vertically to include the ship.
            for y in range(min(stern_y, bow_y), max(stern_y, bow_y) + 1):
                self._update_matrix(stern_x, y, correct_length)
        else: # If the ship is vertical, we update the board vertically to include the ship.
            for x in range(min(stern_x, bow_x), max(stern_x, bow_x) + 1):
                self._update_matrix(x, stern_y, correct_length)
        return True # Returns true only if ship was successfully placed.
    
    def attack(self, x, y):
        hit = False  # Flag to track if a hit occurs.
        # Iterate through every stored ship (There could be a more efficient solution?)
        for ship in self.ships:
            # Check if the indices match the ships stored indices.
            print(ship.indices)
            print(x, y)
            if (x, y) in ship.indices: 
                print("HIT")
                hit = True  # Set flag to True if a hit occurs.
                break
        if not hit:
            print("MISS")
    
    # Checks if the ships overlap.
    def is_overlapping(self, new_ship):
        for ship in self.ships: # This loop checks if the new ship overlaps with any previous ship, returns false if yes.
            if new_ship._is_overlapping(ship):
                print("Ships cannot overlap.")
                return True

    @staticmethod
    # Checks if the ship is the correct length.
    def is_correct_length(stern_x, stern_y, bow_x, bow_y, correct_length):
        length = max(abs(stern_x - bow_x), abs(stern_y - bow_y)) + 1 # Calculate the length.
        if length != correct_length: # If the length isn't the intended length, tell user and return false.
            print(f"The length of ship must be {correct_length}.")
            return False
        return True

    @staticmethod
    # Checks if the ship is diagonal, returns true if it is.
    def is_diagonal(stern_x, stern_y, bow_x, bow_y):
        if stern_x != bow_x and stern_y != bow_y:
            print("Ships must be placed horizontally or vertically\n")
            return True
        return False

     # Could be overkill but maybe we want future logic.
    def _update_matrix(self, i, j, val):
        self.matrix[i][j] = val
        
    def __repr__(self):
        return f"{self.matrix}"