
# logic.py

def process_guess(secret, letter, correct_guesses, wrong_guesses):
   
    if letter in secret:
        correct_guesses.add(letter)
    else:
        wrong_guesses.add(letter)

def has_won(secret, correct_guesses):   

    return set(secret).issubset(correct_guesses)

def has_lost(wrong_guesses, max_lives):
   
    return len(wrong_guesses) >= max_lives


