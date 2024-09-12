from ship import Ship

class Board:

    def __init__(self, name):
        self.name = name
        self.matrix = [[0] * 10 for _ in range(10)] # Initialize a 10x10 matrix with zeroes
        self.ships = [] # Store ships placed on the board.

    def _is_overlapping(self): #used to verify no overlap
        # Iterate through each pair of ships
        for i in range(len(self.ships)):
            for j in range(i + 1, len(self.ships)):
                # If there is any intersection between the sets of ship indices, they overlap
                if not self.ships[i].indices.isdisjoint(self.ships[j].indices):
                    return False  # If any pair of ships overlap, return False
        return True  # If no overlaps are found, return True
    
    # Place a ship on board given indices. returns true if placed successfully, false if not
    def place_ship(self, stern_x, stern_y, bow_x, bow_y, realLength):
        #checks if the ship is diagonal, returns false if it is
        if stern_x != bow_x and stern_y != bow_y:
            print("Ships must be placed horizontally or vertically\n")
            return False
        length = max(abs(stern_x - bow_x), abs(stern_y - bow_y)) + 1 #calculate the length
        if length != realLength: #if the length isn't the intended length, tell user and return false
            print(f"The length of ship must be {realLength}.")
            return False
        vert = (stern_x == bow_x) #determine if the ship is vertical or not
        new_ship = Ship(length, stern_x, stern_y, vert = vert) #create a new ship
        for ship in self.ships: #this loop checks if the new ship overlaps with any previous ship, returns false if yes
            if new_ship._overlaps(ship):
                print("Ships cannot overlap.")
                return False
        self.ships.append(new_ship) #put the ship in the ship array
        if vert: #if the ship is vertical, we update the board vertically to include the ship
            for y in range(min(stern_y, bow_y), max(stern_y, bow_y) + 1):
                self._update_matrix(stern_x, y, length)
        else: #if the ship is vertical, we update the board vertically to include the ship
            for x in range(min(stern_x, bow_x), max(stern_x, bow_x) + 1):
                self._update_matrix(x, stern_y, length)
        return True #returns true only if ship was successfully placed
        #----------------------------------------------
    
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
    
    
     # Could be overkill but maybe we want future logic.
    def _update_matrix(self, i, j, val):
        self.matrix[i][j] = val
        
    def __repr__(self):
        return f"{self.matrix}"