
# input_handler.py
#from utils import get_int  # (optional) if you reuse get_int, else not needed

def get_letter_guess(guessed_letters):
    """
    Prompt until the player enters a valid, new single letter (A–Z).
    `guessed_letters` is a set of letters already tried.
    Returns the uppercase letter.
    """
    while True:

        user_input = input("Enter your next letter: ").strip().upper()

        # 1) Single character check        
        if len(user_input) != 1:
            print("Please enter exactly one letter.\n")
            continue

        # 2) Alphabet check

        if not user_input.isalpha():
            print("That’s not a letter. Please enter A–Z.\n")
            continue

        # 3) New guess check

        if user_input in guessed_letters:
            print(f"You already guessed '{user_input}'. Try another.\n")
            continue

        # 4) Valid new letter

        return user_input


