class Board:

    def __init__(self, size=10):
        self.matrix = [[0] * size for _ in range(size)] # initialize a 10x10 matrix with zeroes

    def _place_ship(self, i, j):
        #still need to code boundary logic and what not, how long the ship is, etc...
        self.matrix[i][j] = 1

    def __repr__(self):
        #for debug purposes
        return f"{self.matrix}"
    
    

    
