'''
Program Name: ship,py
Description: ship.py manages the internal workings of the ships within the game. It is responsible for populating 
    indices and validating some user input.
Inputs: None
Output: None
Code Sources:
Authors: Steve Gan, Sean Hammell, Jacob Leehy, Mario Simental, Matthew Sullivan
Creation Date: 9/9/24
'''
class Ship: # class used to represent ships
    #param: length is an int representing the length of the ship
        #start_row is an int representing the y coordinate of the start of the ship
        #start_col is an int representing the x coordinate of the start of the ship
        #vert is a boolean representing if the ship is vertical or not. Assumes that ships only go down or to the right
    def __init__(self, length: int, start_row: int, start_col: int, vert: bool) -> None:  # constructor for ship - takes ship length, start row and col, and vertical bool
        self.indices = set() #indices is a set containing tuples. Each tuple represents one coordinate
        self._populate_indices(length, start_row, start_col, vert) # calls populate indices

    '''
    Defines a method that is used to populate the indices used by the ships. 
    '''
    def _populate_indices(self, length: int, start_row: int, start_col: int, vert: bool) -> None: # Add the indices a ship takes up to a set.
        if vert: # if vertical
            for col in range(length): # iterate over length of ship
                self.indices.add((start_row, start_col + col))  # add the needed coordinates
        else: # else not vertical
            for row in range(length): # iterate over length of ship
                self.indices.add((start_row + row, start_col))  # add the needed coordinates
    
    '''
    Defines a method that is used to determine if ships overlap.
    Returns a boolean indicating the outcome.
    '''
    def is_overlapping(self, otherShip: 'Ship') -> bool: # Check if a ship overlaps another ship.
        for indices in otherShip.indices: # iterate over indices in other ship
            if indices in self.indices: # check if indices is in current ships indices
                return True # return true
        return False # return false
    
    def __repr__(self) -> str: # magic method to help with printing
        return f"Indices: {self.indices}" # print the indices
