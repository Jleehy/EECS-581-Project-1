class Board:

    def __init__(self):
        self.matrix = [[0] * 10 for _ in range(10)] # initialize a 10x10 matrix with zeroes
        #TODO: add a self.ships = [] to keep track of ship objects per board

    def _place_ship(self, start_i, start_j, end_i, end_j):
        #TODO: change this to use the ships class. 
        
        print(f"{start_i},{start_j}: {end_i},{end_j}") # debug
        if start_i == end_i:  # horizontal ship placement
            print("HORIZONTAL") # debug
            for j in range(min(start_j, end_j), max(start_j, end_j) + 1):
                self.matrix[start_i][j] = 1
        elif start_j == end_j:  # vertical ship placement
            print("VERTICAL") # debug
            for i in range(min(start_i, end_i), max(start_i, end_i) + 1):
                self.matrix[i][start_j] = 1
        else:
            raise ValueError("Ships must be placed either horizontally or vertically.")
        
        
    def __repr__(self):
        #for debug purposes
        return f"{self.matrix}"
    
    

    
