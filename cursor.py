'''
Program Name: cursor.py
Description: cursor.py is responsible for making the game UI user readable. It also obscures important information.
Inputs: None
Output: Clears text from the console and moves the cursor.
Code Sources:
Authors: Steve Gan, Sean Hammell, Jacob Leehy, Mario Simental, Matthew Sullivan
Creation Date: 9/9/24
'''
def move_to(n: int) -> None: # Moves the cursor to the beginning of line n.
    print(f"\x1B[{n};0H", end = "") # is used to move the cursor to a specific position in the terminal using ANSI escape codes

def move_up(n: int) -> None: # Moves the cursor to the beginnning of the previous line, n lines up.
    print(f"\x1B[{n}F", end = "") # is used to move the cursor to a specific position in the terminal using ANSI escape codes

def erase() -> None: # Erases everything from the cursor to the end of the screen.
    print("\x1B[0J", end = "") # clears terminal screen
