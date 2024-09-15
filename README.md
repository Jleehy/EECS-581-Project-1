
# Battleship - EECS 581 Project 1

## Authors
- **Steve Gan** - [GitHub](https://github.com/qgan99) 
- **Sean Hammell** - [GitHub](https://github.com/seanhammell)
-  **Jacob Leehy** - [GitHub](https://github.com/Jleehy) 
- **Mario Simental** - [GitHub](https://github.com/aepii) 
- **Matthew Sullivan** - [GitHub](https://github.com/matthewsullivan1)

## Overview
This project is a terminal-based **Battleship Game**. We decided to utilize the **Facade Design Pattern** to create our program's overall structure. This pattern allowed for modularization- simplifying the interaction between the main driver, the application (high-level interface), the game boards (game logic), and the ships.

## Structure
The **Facade Design Pattern** allows for a complex system to be simplified by having an interface hide the internal complexities. The `App` class acts as the facade, taking care of the complexities- allowing for communication between `main.py` (the driver), `board.py` (the player's board), `ship.py` (ship object), and `cursor.py` (handles terminal clearing).
