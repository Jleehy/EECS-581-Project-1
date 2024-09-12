from ship import Ship

class Board:

    def __init__(self, name):
        self.name = name
        self.matrix = [[0] * 10 for _ in range(10)] # Initialize a 10x10 matrix with zeroes
        self.ships = [] # Store ships placed on the board.

    def _is_valid_move(self): #used to verify no overlap
        # Iterate through each pair of ships
        for i in range(len(self.ships)):
            for j in range(i + 1, len(self.ships)):
                # If there is any intersection between the sets of ship indices, they overlap
                if not self.ships[i].indices.isdisjoint(self.ships[j].indices):
                    return False  # If any pair of ships overlap, return False
        return True  # If no overlaps are found, return True
    
    # Place a ship on board given indices.
    def place_ship(self, stern_x, stern_y, bow_x, bow_y):      
        # Horizontal ship placement
        if stern_x == bow_x: 
            size = abs(stern_y - bow_y) + 1

            new_ship = Ship(size, stern_x, stern_y, vert = False) # Create a ship object with i,j indices and whether its placed vertically. 
            self.ships.append(new_ship) # Store the ship

            if not self._is_valid_move(): #---------------------------------------verifies no overlap
                del new_ship
                self.ships.pop()
                return False

             # Iterate through the x axis.
            for y in range(min(stern_y, bow_y), max(stern_y, bow_y) + 1):
                self._update_matrix(stern_x, y, 1)
            return True
        
        # Vertical ship placement
        elif stern_y == bow_y: 
            size = abs(stern_x - bow_x) + 1

            new_ship = Ship(size, stern_x, stern_y, vert = True) # Create a ship object with i,j indices and whether its placed vertically. 
            self.ships.append(new_ship) # Store the ship

            if not self._is_valid_move(): #-----------------------------------------verifies no overlap
                del new_ship
                self.ships.pop()
                return False

            # Iterate through the y axis.
            for x in range(min(stern_x, bow_x), max(stern_x, bow_x) + 1):
                self._update_matrix(x, stern_y, 1)
            return True
        #----------------------------------------------

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
    
    # Return if the coordinate is valid.
    def is_valid_coordinate(self, x, y):
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
