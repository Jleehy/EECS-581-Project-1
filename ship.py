class Ship:
    #param: length is an int representing the length of the ship
        #start_row is an int representing the y coordinate of the start of the ship
        #start_col is an int representing the x coordinate of the start of the ship
        #vert is a boolean representing if the ship is vertical or not. Assumes that ships only go down or to the right
    def __init__(self, length, start_row, start_col, vert): 
        self.indices = set() #indices is a set containing tuples. Each tuple represents one coordinate
        self._populate_indices(length, start_row, start_col, vert)

    # Add the indices a ship takes up to a set.
    def _populate_indices(self, length, start_row, start_col, vert):
        if vert:
            for col in range(length):
                self.indices.add((start_row, start_col + col))  # corrected
        else:
            for row in range(length):
                self.indices.add((start_row + row, start_col))  # corrected
    
    # Check if a ship overlaps another ship.
    def _is_overlapping(self, otherShip):
        for indices in otherShip.indices:
            if indices in self.indices:
                return True
        return False
    
    def __repr__(self):
        return f"Indices: {self.indices}"
