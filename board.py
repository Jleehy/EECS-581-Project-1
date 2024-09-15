'''
Program Name: board.py
Description: bpard.py maintains the board and controls ship placement as well as user input validation.
    It also controls much of the turn logic.
Inputs: The game takes user input periodically during the game.
Output: The game outputs text to the console
Code Sources:
Authors: Steve Gan, Sean Hammell, Jacob Leehy, Mario Simental, Matthew Sullivan
Creation Date: 9/9/24
'''
import cursor # import for cursor
from ship import Ship # import for Ship

class Board: # board class to manage the game boards needed for battleship

    def __init__(self, name: str) -> None: # constructor that takes a name
        self.name = name # object name is name
        self.matrix = [[0] * 10 for _ in range(10)] # Initialize a 10x10 matrix with zeroes.
        self.ships = [] # Store ships placed on the board.
        self.shots = set() # tracks what coordinates this ship has fired at

    '''
    Defines a method that places a ship. It takes two sets of coordinates, one for each end of the ship.
    It also takes the length the ship should be. It also validates the users input and determines if reinput
    is necessary. It updates the board matrix as needed. Returns a boolean representing a successful/unsuccessful
    operation.
    '''
    def place_ship(self, stern_row: int, stern_col: int, bow_row: int, bow_col: int, correct_length: int) -> bool: # Place a ship on board given indices. returns true if placed successfully, false if not.
        
        if self.is_diagonal(stern_row, stern_col, bow_row, bow_col): # Check if the ship is being placed diagonally.
            return False # return false

        if not self.is_correct_length(stern_row, stern_col, bow_row, bow_col, correct_length): # Check if the ship is the correct length.
            return False # return false
        
        vert_bool = (stern_row == bow_row) # Determine if the ship is vertical or not by comparing the coordinate rows
        if stern_row > bow_row or stern_col > bow_col: # checks to see if the coordinates are oriented in increacing order. i.e coordinates are in left-right or up-down order
            stern_row, bow_row = bow_row, stern_row # if not correct, swap the rows
            stern_col, bow_col = bow_col, stern_col # swap cols
        new_ship = Ship(correct_length, stern_row, stern_col, vert=vert_bool) # Create a new ship using relevent coordinates and a boolean to see if vertical. also passes expected ship length.

        if self.is_overlapping(new_ship): # Check if the ship overlaps with other ships.
            return False # return false
            
        self.ships.append(new_ship) # Put the ship in the ship array.

        if vert_bool: # If the ship is vertical, we update the board vertically to include the ship.
            for col in range(min(stern_col, bow_col), max(stern_col, bow_col) + 1): # iterates over all column indices between two given columns (stern_col and bow_col), regardless of which one is smaller
                self._update_matrix(stern_row, col, correct_length) # update the matrix accordingly
        else: # If the ship is vertical, we update the board vertically to include the ship.
            for row in range(min(stern_row, bow_row), max(stern_row, bow_row) + 1): # iterate over all row indices between two given row (stern_row and bow_row), regardless of which one is smaller
                self._update_matrix(row, stern_col, correct_length) # update matrix accordingly

        return True # Returns true only if ship was successfully placed.

    '''
    Defines a method that checks if an attack has already been made and adds it to the attack log if not.
    Returns a boolean value if the attack is invalid due to repitition.
    '''
    def attack(self, row: int, col: int) -> bool: # Record an attack made by this player, returning if the coordinate was already attacked.
        if (row, col) in self.shots: # if coordinate is already in shots
            return False # return false

        self.shots.add((row, col)) # add new coordinate to shots
        return True # return true

    '''
    Defines a method that handles the logic needed to determine if an attack hits, misses, or sinks a ship.
    It updates the board as needed to represent each of these cases. It returns two boolean values
    which indicate if a hit, miss, or sink was achieved.
    '''
    def defend(self, row: int, col: int) -> tuple[bool, bool]: # Handle an attack against this player's board, return hit status.
        hit = False  # Flag to track if a hit occurs.
        sunk = False # Flag to track if a sink occurs.
        for ship in self.ships: # iterate over all ships
            # Check if the (row, col) match any of the ship's indices
            if (row, col) in ship.indices: # if coordinate is in the list of ship indices
                ship.indices.remove((row, col))  # Remove the hit index from the ship
                hit = True  # Set flag to True if a hit occurs
                self._update_matrix(row, col, 6) # Indicate hit status, red.
                if not ship.indices: # if nothing left in indices
                    sunk = True # Set flag to True if a sink occurs.
                break # break
            
        return hit, sunk # return hit and sunk booleans
    
    '''
    Defines a method to iterate over the ships and determine if any inputs overlap.
    Returns a boolean value to specify if ships overlap.
    '''
    def is_overlapping(self, new_ship: Ship) -> bool: # Checks if the ships overlap.
        for ship in self.ships: # This loop checks if the new ship overlaps with any previous ship, returns true if yes.
            if new_ship.is_overlapping(ship): # calls helper function to determine overlap
                cursor.move_to(23) # move cursor
                cursor.erase() # erase old text
                print("Ships cannot overlap") # print no overlap allowed
                return True # return true
        return False # return false

    '''
    Defines a method that checks the length of a ship to ensure that ships are the correct length.
    It returns a boolean value indicating if the ship has the correct length.
    '''
    @staticmethod # static
    def is_correct_length(stern_row: int, stern_col: int, bow_row: int, bow_col: int, correct_length: int) -> bool: # Checks if the ship is the correct length.
        length = max(abs(stern_row - bow_row), abs(stern_col - bow_col)) + 1 # Calculate the length.
        if length != correct_length: # If the length isn't the intended length, tell user and return false.
            cursor.move_to(23) # move cursor
            cursor.erase() # delete old text
            print(f"The length of ship must be {correct_length}") # tell required length
            return False # return false
        return True # return true

    '''
    Defines a method that is used to determine if a ship is diagonal. If it is diagonal, it 
    tells the user and forces reinput. Returns a boolean representing the orientation
    of the ship.
    '''
    @staticmethod # static
    def is_diagonal(stern_row: int, stern_col: int, bow_row: int, bow_col: int) -> bool: # Checks if the ship is diagonal, returns true if it is.
        if stern_row != bow_row and stern_col != bow_col: # if rows and columns do not match
            cursor.move_to(23) # move cursor
            cursor.erase() # erase old text
            print("Ships must be placed horizontally or vertically") # print orientation requirement
            return True # return true
        return False # return false

    '''
    Defines a method used to update the board matrix as needed.
    '''
    # Could be overkill but maybe we want future logic.
    def _update_matrix(self, row: int, col: int, val: int) -> None: # function to update the matrix. takes row, col, and update value
        self.matrix[row][col] = val # sets matrix coordinate to the desired value

    '''
    Defines a method used to dertmine if all ships have been sunk or not. Returns a boolean
    representing the outcome.
    '''
    def all_ships_sunk(self) -> bool: # function to determine if all ships are sunk - used for win condition
        return all(len(ship.indices) == 0 for ship in self.ships) # If all ships have no remaining coordinates (i.e., no part of the ship is still on the board), return True
        
    def __repr__(self) -> str: # magic method for printing
        return f"{self.matrix}" # makes printing easy. just print matrix
