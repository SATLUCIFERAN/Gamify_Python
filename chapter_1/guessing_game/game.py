
# game.py
import random

from utils import get_int

def main():
    print("Welcome to Number Guessing!\n")
    secret   = random.randint(1, 100)
    attempts = 0

    while True:
        # Unified prompt, validation, and conversion:
        guess = get_int("Guess a number between 1 and 100: ")
        attempts += 1

        if guess < secret:
            print("Too low! Try again.\n")
        elif guess > secret:
            print("Too high! Try again.\n")
        else:
            print(f"Congratulations! You guessed it in {attempts} tries.\n")
            break

if __name__ == '__main__':
    main()

