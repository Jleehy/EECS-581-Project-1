'''
Program Name: main.py (Battleship)
Description: This is the main.py for a python Battleship game designed to be played by two players on a single computer. 
    It mimics a real game of Battleship by allowing each player to place a specified number of ships and begin blindly 
    attacking the opposing player until one player has sunk all of the opposing ships. main.py controls the primary gameplay loop.
Inputs: The game takes user input periodically during the game.
Output: The game outputs text to the console
Code Sources:
Authors: Steve Gan, Sean Hammell, Jacob Leehy, Mario Simental, Matthew Sullivan
Creation Date: 9/9/24
'''
from app import App # import for app
from board import Board # import for board
import cursor # import for cursor
import os # import for os

# ANSI Escape Sequences Reference: https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797

'''
Defines a main function that it used to maintain and run the primary game loop.
Takes user input and calls the other classes as needed to run the game.
'''
def main(): # main function to handle the main gameloop
    cursor.move_to(0) # move cursor
    cursor.erase() # erase old text

    print("Important!\n") # print message
    terminal_size = os.get_terminal_size() # variable to get terminal size
    if terminal_size[0] > 79 and terminal_size[1] > 39: # if terminal size meets minimum requirements
        print(f"Good news! Your terminal size is {terminal_size[0]}x{terminal_size[1]}!\n") # print message
    else: # else
        print(f"Your terminal size is {terminal_size[0]}x{terminal_size[1]}, which is... concerning, to say the least.\n") # print warning message

    print("For the best Battleship experience, we recommend a size of 80x40 or more. This") # print message
    print("is to keep secret information secret and make sure everything displays as it") # print message
    print("should.\n") # print message
    input("Press Enter to acknowledge...") # print message

    cursor.move_to(0) # move cursor
    cursor.erase() # erase old text

    # Create each player's board.
    name1 = input("Enter the first player's name: ") # player 1 name input
    name2 = input("Enter the second player's name: ") # player 2 name input
    player1 = Board(name1) # create player 1 board
    player2 = Board(name2) # create player 2 board
    players = [player1, player2] # list of players
    
    app = App(player1, player2) # Create the Battleship app.

    app.prompt_num_ships() # Prompt the user to enter the number of ships to be played.

    # Give each player a chance to place their ships.
    for player in players: # iterate over players
        cursor.erase() # erase old text
        action = input(f"\n{player.name}, press Enter to begin placing your ships...") # prompt confirmation
        app.check_quit(action) # check if q or Q

        cursor.move_up(1) # move cursor
        cursor.erase() # erase old text

        print(player.name + "'s turn to place their ships") # print player and turn notification

        for ship in range(app.num_ships): # For each ship in the player's arsenal.
            cursor.erase() # erase old text
            app.print_board(player) # print board for current player

            print("Coordinate input format: A1") # message about coordinates
            print("Valid x-coordinates: A - J") # valid x range
            print("Valid y-coordinates: 1 - 10\n") # valid y range

            while True: # while true
                # If the ship size is 1, assign both bow and stern to the same coordinate.
                if ship == 0: # if first ship, aka 1x1
                    stern = bow = app.prompt_ship_coordinate(ship, "rear") # stern and bow same coordinate
                else: # else
                    stern = app.prompt_ship_coordinate(ship, "rear") # Rear coordinate of the ship.
                    bow = app.prompt_ship_coordinate(ship, "front") # Front coordinate of the ship.

                # Place the player's ship on their board.
                if app.place_ship(player, stern, bow, ship + 1): # place curently input ship
                    break # break if invalid

            cursor.move_to(6) # Move the cursor to the line after "Player #'s turn to place their ships".

        cursor.erase() # erase old text
        app.print_board(player) # Ensure board prints on last turn.

        action = input(f"{player.name}, press Enter after reviewing your ship placements...") # Ask the player if they are ready to turn the device over to the second player.
        app.check_quit(action) # check if q or Q entered

        # prepare to clear the screen for Player 2 to place their ships.
        cursor.move_to(4) # Move the cursor to the line after "Enter the number of ships" to

    # Begin the game loop.
    current_player = 0 # set initial player
    while True: # while true
        attacker = players[current_player] # attacker is current player
        defender = players[abs(current_player - 1)] # defender is other player

        cursor.move_to(0) # move cursor
        cursor.erase() # erase old text

        print(attacker.name + "'s turn to attack\n") # print current attacker
        action = input(f"{attacker.name}, press Enter to begin attacking...") # confirm ready to attack
        app.check_quit(action) # check for q or Q

        cursor.move_up(1) # move cursor
        cursor.erase() # erase old text

        print("Your Board") # Print the current player's board
        app.print_board(attacker) # print attacker board

        print("Enemy's Board") # Print the enemy's board (the other player's board, censored)
        app.print_board(defender, censored=True) # print censored version of defending board

        while True: # while true
            coord = app.prompt_attack_coordinate() # get attack coordinate
            attack_result = app.attack(attacker, defender, coord) # assign string generated from attack
            if len(attack_result) == 0: # Don't allow the attacker to attack the same coordinate twice - prompt returns "" if same spot
                cursor.move_to(31) # move cursor
                cursor.erase() # erase old text
                print("You've already attacked that coordinate") # print warning
                continue # continue

            # Erase everything after "Enemy's Board"
            cursor.move_to(18) # move cursor
            cursor.erase() # erase old text

            # Print the enemies board with the result of the attack
            app.print_board(defender, censored=True) # print enemy board
            print(attack_result) # print result

            break # break

        if defender.all_ships_sunk(): # Check if all ships of the enemy have been sunk
            print(f"\n{attacker.name} wins! All of {defender.name}'s ships have been sunk!\n") # print victory message
            break  # Exit the game loop to end the game

        # Ask the player if they are ready to turn the device over to the second player.
        action = input(f"\n{attacker.name}, press Enter when you're done reviewing your attacks...") # confirm ready
        app.check_quit(action) # check for q or Q

        current_player = abs(current_player - 1) # Switch to the other player

if __name__ == "__main__": # magic method for main
    main() # call main
