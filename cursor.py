# Moves the cursor to the beginning of line n.
def move_to(n):
    print(f"\x1B[{n};0H", end = "")

# Moves the cursor to the beginnning of the previous line, n lines up.
def move_up(n):
    print(f"\x1B[{n}F", end = "")

# Erases everything from the cursor to the end of the screen.
def erase():
    print("\x1B[0J", end = "")
