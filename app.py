'''
Program Name: app.py
Description: app.py controls several fundamental aspects of the gameplay loop, including user prompts, board maintenence,
    and input processing.
Inputs: The game takes user input periodically during the game.
Output: The game outputs text to the console
Code Sources:
Authors: Steve Gan, Sean Hammell, Jacob Leehy, Mario Simental, Matthew Sullivan
Creation Date: 9/9/24
'''
import cursor # import for cursor
import sys # import for sys

class App: # App class to handle the general gameplay loop
    def __init__(self, player1, player2, num_ships=0): # constrcutor for app, takes two players and a number of ships
        # 0: blank, 1 - 5: ships of different colors, 6: red hit, 7: white miss
        # 1: blue
        # 2: green
        # 3: yellow
        # 4: light purple
        # 5: cyan
        self.config = {0: "□", 1: "\033[34m■\033[0m", 2: "\033[32m■\033[0m", 3: "\033[33m■\033[0m", 4: "\033[35m■\033[0m", 5: "\033[36m■\033[0m", 6: "\033[31m•\033[0m",     7: "\033[37m•\033[0m"} # defines the configuration for each of the symbols used by the board
        self.player1 = player1 # Holds a board object for Player 1.
        self.player2 = player2 # Holds a board object for Player 2.
        self.num_ships = num_ships # sets number of ships

    # Place a ship on a player's board and validate placement. 
    # Returns False if ship placement is unsuccessful and true if it is
    def place_ship(self, player, stern, bow, ship_size): #function which places a ship on the board
        # Create indices for the stern and bow.
        # Note: There is no need to wrap this in a try-except because
        # is_valid_coordinate ensures stern[1:] and bow[1:] can be cast
        # to integers.
        stern_row, stern_col, bow_row, bow_col = self.literals_to_indices(stern, bow) # This passes the stern and bow coordinates to a function which separates the coordinates into two dimentions each. These dimensions are assigned to the four variables which will be used to place the ships on the board
        return player.place_ship(stern_row, stern_col, bow_row, bow_col, ship_size) # player.place_ship checks for validity
    
    '''
    Handles the attacking process by generating a response string and calling other methods to update the boards as needed.
    It also indirectly allows the boards to be printed to the players as needed.
    '''
    def attack(self, attacker, defender, pos): # defines a function that will be used to attack an oposing board
        attack_result = "" # instantiate var as string for outcome
        row, col = self.literals_to_indices(pos) # converts the attack position to coordinates that can be used on the board
        if not attacker.attack(row, col): # calls boards attack method to determine if that space has already been attacked
            return attack_result # If attacked, return result

        hit, sunk = defender.defend(row, col) # calls boards defend method to determing the outcome of the attack using the defenders board. Assigns boolean values to hit and sunk
        
        if hit: # if hit
            attack_result += f"Hit at {pos}!" # attack result becomes a hit at the position
            if sunk: # if sunk
                attack_result += "\nYou sunk a ship!" # appends that a ship has been sunk
        else: #else
            attack_result += f"Missed at {pos}..." # result is a miss
            defender._update_matrix(row, col, 7)  # Indicate miss on board with white.

        return attack_result # returns the final result as a string

    '''
     Prints the board by generating the axes labels and building the needed strings to represent the board rows.
     It also consideres what information should be displayed to the user by censoring certain information if needed.
    '''   
    # Print a player's board with literal coordinates.
    def print_board(self, player, censored=False): #defines a method that prints the board, taking a player and censored boolean as input
        column_headers = "\n   " + "   ".join("A B C D E F G H I J".split()) # add column headers (A-J)
        print(column_headers) # print the column headers

        # create the formatted board with row numbers and symbols
        for i, row in enumerate(player.matrix): # loops through each row of the matrix, with i being the row index and row being the content of that row
            # add row numbers (1-10), then the formatted row contents
            if censored: # if censored
                row_str = f"{i+1:2} " + " | ".join(self.config[0] if cell in range(1,6) else self.config[cell] for cell in row) # each cell in the row is replaced either by \ (self.config[0]) if it is within a certain range (1 to 5) or by another value from self.config[cell] if it's outside that range. This censors the board by removing certain symbols from the defenders board
            else: #else
                row_str = f"{i+1:2} " + " | ".join(self.config[cell] for cell in row) # creates a formatted string to be used in printing the board
            print(row_str) # print row string

        print() #new line

    '''
    Converts literal coordinates to indices by breaking each coordinate into two chunks. This is completed by 
    parsing the user input into manageable coordinates that the rest of the game logic can use. 
    It also considers the number of coordinates it will need to parse. 
    Returns parsed coordinate(s).
    '''
    @staticmethod #static
    def literals_to_indices(pos1, pos2=None): # defines a method to convert literals to usable indices
        def parse_position(pos): # helper func to parse pos
            row = int(pos[1:]) - 1 # extracts everything after the first char and converts to int. i.e. "A10" -> 10
            col = ord(pos[0]) - ord('A') # extracts first character and subtracts A ascii code. This essentially makes a letter based index system into a zero based index system
            return row, col # return the new row and col

        pos1_row, pos1_col = parse_position(pos1) # parse position on first position

        if pos2 is None: # if pos2 is none (i.e in the case of an attack)
            return pos1_row, pos1_col # just return the pos1 info
        else: # else
            pos2_row, pos2_col = parse_position(pos2) # parse pos2
            return pos1_row, pos1_col, pos2_row, pos2_col # return all four values

    @staticmethod # static
    # Check if the program should exit.
    def check_quit(action): # function to check to see if Q is entered and exit the program if it is
        if len(action) == 0: # nothing entered
            return # return
        if action[0].upper() == 'Q': # if the action is q or Q
            sys.exit("\nExiting...\n") # exit via system

    '''
    This method prompts the user for ship coordinates and validates those coordinates. It also cleans 
    the board as is needed. It returns the coordinate if it is valid and reprompts the user if not.
    '''
    def prompt_ship_coordinate(self, ship_number, part): # Prompt the user for a ship coordinate, ensuring a valid input.
        while True: # while true
            coord = input(f"Coordinate for the {part} of ship {ship_number + 1}, with dimensions 1x{ship_number+1}: ").strip().upper()[:3] # get coordinate and specify ship side, number, and dimensions to the user
            self.check_quit(coord) # check to see if q or Q
            if self._is_valid_coordinate(coord[0], coord[1:]): # send to coordinate checker to see if valid - pass as two parts
                return coord # retur the coordinate if valid

            # Clear the last line of text to prompt the user again since the coordinate was invalid.
            cursor.move_up(1) # move cursor
            cursor.erase() # erase old text
    
    '''
    This method prompts the user for attack coordinates and validates those coordinates. 
    It returns the coordinate if valid. Otherwise, it reprompts the user.
    '''
    def prompt_attack_coordinate(self): # Prompt the user for a ship coordinate to attack, ensuring a valid input.
        while True: # while true
            coord = input("Coordinate to attack: ").strip().upper()[:3] # get attack coordinate from user
            self.check_quit(coord) # check to see if q or Q entered

            # Woe betide ye who try coord[1:] on a string with less than 2 characters.
            if len(coord) < 2: # verify length less than 2
                cursor.move_up(1) # move cursor
                cursor.erase() # erase old text
                continue # continue in loop, aka reprompt

            if self._is_valid_coordinate(coord[0], coord[1:]): # If valid coordinate
                return coord # return the coordinate

    '''
    This method prompts the user to enter the number of ships they want to play with.
    It also checks the input to ensure that it meets game specifications.
    '''
    def prompt_num_ships(self): # Prompt the user for the number of ships to play with, ensuring a valid input.
        while True: # while true
            num_ships = input("Enter the number of ships (1 - 5): ") # prompt for number of ships
            self.check_quit(num_ships) # check if q or Q entered
            if num_ships.isnumeric(): # verify numeric
                num_ships = int(num_ships) # convert to int
                if num_ships > 0 and num_ships < 6: # verify ships between 1 and 5
                    self.num_ships = num_ships # set num ships to num ships
                    return # return
    
    '''
    This method verifies that a give coordinate is valid. It does this by verifying the row and column
    of what is entered. Returns a boolean representing the validity of the coordinate.
    '''
    @staticmethod # static
    def _is_valid_coordinate(col, row): # Return if the coordinate is valid.
        # Valid x-coordinates: A - J.
        if col < 'A' or col > 'J': # col must be between A and J
            return False # retur  false if not A - J

        # Protect against ValueErrors since y may not be an int.
        try: # try 
            # Valid y-coordinates: 1 - 10.
            if int(row) < 1 or int(row) > 10: # if row is int less than 1 or greater than 10
                return False # return false
        except ValueError as e: # except value error
            return False # return false

        return True # return true
