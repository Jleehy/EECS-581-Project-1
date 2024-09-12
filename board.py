from ship import Ship

class Board:

    def __init__(self, name):
        self.name = name
        self.matrix = [[0] * 10 for _ in range(10)] # Initialize a 10x10 matrix with zeroes
        self.ships = [] # Store ships placed on the board.

    # Place a ship on board given indices.
    def place_ship(self, start_i, start_j, end_i, end_j):      

        # Don't allow diagonal ship placement.
        if not start_i == end_i and not start_j == end_j:
            raise ValueError("Ships must be placed either horizontally or vertically.")

        # Horizontal ship placement
        if start_i == end_i: 
            print("PLACED HORIZONTALLY") # DEBUG PURPOSES
            size = abs(start_j - end_j) + 1

            new_ship = Ship(size, start_i, start_j, vert=False) # Create a ship object with i,j indices and whether its placed vertically. 
            self.ships.append(new_ship) # Store the ship

             # Iterate through the x axis.
            for current_j in range(min(start_j, end_j), max(start_j, end_j) + 1):
                self._update_matrix(start_i, current_j, 1) # Could be overkill but maybe we want future logic.
        # Vertical ship placement
        elif start_j == end_j: 
            print("PLACED VERTICALLY") # DEBUG PURPOSES
            size = abs(start_i - end_i) + 1

            new_ship = Ship(size, start_i, start_j, vert=True) # Create a ship object with i,j indices and whether its placed vertically. 
            self.ships.append(new_ship) # Store the ship

            # Iterate through the y axis.
            for current_i in range(min(start_i, end_i), max(start_i, end_i) + 1):
                self._update_matrix(current_i, start_j, 1) # Could be overkill but maybe we want future logic.

    def attack(self, i, j):
        hit = False  # Flag to track if a hit occurs.
        # Iterate through every stored ship (There could be a more efficient solution?)
        for ship in self.ships:
            # Check if the indices match the ships stored indices.
            if (i, j) in ship.indices: 
                print("HIT")
                hit = True  # Set flag to True if a hit occurs.
                break
        if not hit:
            print("MISS")
    
     # Could be overkill but maybe we want future logic.
    def _update_matrix(self, i, j, val):
        self.matrix[i][j] = val
        
    def __repr__(self):
        return f"{self.matrix}"
