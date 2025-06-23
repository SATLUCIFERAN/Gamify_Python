# utils.py

import os

def get_int(prompt):
    
    while True:
        s = input(prompt)            # “Row: ” or “Col: ”
        if s.isdigit():              # Is every character 0–9?
            return int(s)            # Yes → convert and hand back
        print("That’s not a whole number. Try again!\n")



def clear_screen():
    """
    Clear the terminal (Windows or Unix) so the board redraws cleanly.
    """
    if os.name == "nt":            # Windows systems use 'cls'
        os.system("cls")
    else:                           # macOS/Linux use 'clear'
        os.system("clear")
