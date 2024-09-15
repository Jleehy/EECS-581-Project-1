
# Battleship - EECS 581 Project 1

## Authors
- **Steve Gan** - [GitHub](https://github.com/qgan99) 
- **Sean Hammell** - [GitHub](https://github.com/seanhammell)
-  **Jacob Leehy** - [GitHub](https://github.com/Jleehy) 
- **Mario Simental** - [GitHub](https://github.com/aepii) 
- **Matthew Sullivan** - [GitHub](https://github.com/matthewsullivan1)

## Overview
This project is a terminal-based **Battleship Game**. We decided to utilize the **Facade Design Pattern** to create our program's overall structure. This pattern allowed for modularization- simplifying the interaction between the main driver, the application (high-level interface), the game boards (game logic), and the ships.

## Design Pattern
The **Facade Design Pattern** allows for a complex system to be simplified by having an interface hide the internal complexities. The `App` class acts as the facade, taking care of the complexities- allowing for communication between `main.py` (the driver), `board.py` (the player's board), `ship.py` (ship object), and `cursor.py` (handles terminal clearing).

## Code Structure

### Terminology
There are several use of terminology within the code:

`Literal`: Refers to the coordinates of the board- with the following format: 
- **X-Coordinate:** A-J
- **Y-Coordinate:** 1-10
- **Format:** XY

`Index/Indices`: Refers to the coordinates an array uses. 
- `literals_to_indices`, a helper function in the `App` class,  translates the literals to indices.
-  **Column:** 0-9
- **Row:** 0-9
-  **NOTE:** An array is accessed as: 
```
Array[row][column]
```

### `main.py` - Game Driver
This is the starting point for the game. It is responsible for the primary gameplay loop.
1. **I/O:** Gets player names, number of ships to be played, prompts for ship placements, and ship attacks.
2. **Initialization:** Initializes an `App` object and two players with `Board` objects.
3. **Gameplay Loop:** Manages turns between players, allowing them to place ships and attack each other's boards.
4. **Game Logic:** Makes calls to `App` to handle ship placement, ship attacks and board rendering.

### `app.py` - The Facade
The `App` class provides a simplified interface for interacting with the players' `Board` objects and managing the flow of the game. 

**NOTE:** *Literals* are passed to calls made to `App`.

- `place_ship`: Place ships on the board given literal position and ship size.
- `attack`: Manage attacks made by the player.
- `print_board`: Print a player's board. Can be censored if you want to hide ship placements.
- `literals_to_indices`: Converts *literal* coordinates to *indices*.
- `check_quit`: Checks if Q is entered into prompts, which exits the program.
- `prompt_ship_coordinate`: Prompts user for a ship coordinate (*literal*). 
- `prompt_ship_coordinate`: Prompts user for an attack coordinate (*literal*).
- `prompt_num_ships`: Prompts the user for the number of ships to be played with.
- `_is_valid_coordinate`: Helper function to determine if a given coordinate (*literal*) is valid.

### `board.py` - Player's Board
