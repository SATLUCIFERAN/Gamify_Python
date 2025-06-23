# game.py(before refractor)

import random

def main():
    
    print("Welcome to Number Guessing!\n")
    secret   = random.randint(1, 100)
    attempts = 0

    while True:
        guess_str = input("Guess a number between 1 and 100: ")
        attempts += 1

        # Input validation
        if not guess_str.isdigit():
            print("Please enter a whole number.\n")
            continue

        guess = int(guess_str)

        if guess < secret:
            print("Too low! Try again.\n")
        elif guess > secret:
            print("Too high! Try again.\n")
        else:
            print(f"Congratulations! You guessed it in {attempts} tries.\n")
            break

if __name__ == '__main__':
    main()






