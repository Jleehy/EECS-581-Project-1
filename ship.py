class Ship:
    #param: length is an int representing the length of the ship
        #startx is an int representing the x coordinate of the start of the ship
        #starty is an int representing the y coordinate of the start of the ship
        #vert is a boolean representing if the ship is vertical or not. Assumes that ships only go down or to the right
    def __init__(self, length, start_x, start_y, vert): 
        self.health = length
        self.coor[None] * length #coor is an array of tuples. Each tuple represents one coordinate and it's hit status
        if vert:
            for i in range(length):
                self.coor[i] = (start_x, start_y + i)
        else :
            for i in range(length):
                self.coor[i] = (start_x + i, start_y)

    #returns the coor
    def coor(self):
        return self.coor
    
    #when a ship is hit, returns 1 if it is sunk, returns 0 if not
    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return 1
        else:
            return 0
    