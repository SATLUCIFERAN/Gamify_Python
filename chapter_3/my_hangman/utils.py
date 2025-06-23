
# utils.py
import os
import random

def clear_screen():
    """Clear the terminal (Windows or Unix) so the display redraws cleanly."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def load_wordlist(path="wordlist.txt"):
    """
    Read a file of words (one per line), clean each entry,
    and return a list of uppercase words.
    """
    words = []
    
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            word = line.strip()      # Remove whitespace and newline
            if word:                 # Skip empty lines
                words.append(word.upper())
    return words

def choose_secret(words):
    """
    Return one random word from the list.
    """
    return random.choice(words)


