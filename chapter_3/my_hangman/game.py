

# game.py
from utils          import clear_screen, load_wordlist, choose_secret
from display        import show_word_progress, show_used_letters, show_gallows
from logic          import process_guess, has_won, has_lost
from input_handler  import get_letter_guess

def main():
    # 1) Setup
    words           = load_wordlist("wordlist.txt")
    secret          = choose_secret(words)
    correct_guesses = set()
    wrong_guesses   = set()
    max_lives       = 6

    # 2) Game loop
    while True:
        clear_screen()

        # 2.1) Show gallows art
        print(show_gallows(len(wrong_guesses), max_lives))

        # 2.2) Show word with blanks and reveals
        print("Word:", show_word_progress(secret, correct_guesses))

        # 2.3) Show used letters
        
        all_guesses = correct_guesses.union(wrong_guesses)
        print("Used letters:", show_used_letters(all_guesses))
        print(f"Lives remaining: {max_lives - len(wrong_guesses)}\n")

        # 2.4) Get player's next letter
        guess = get_letter_guess(all_guesses)

        # 2.5) Update game state
        process_guess(secret, guess, correct_guesses, wrong_guesses)

        # 2.6) Check for win
        if has_won(secret, correct_guesses):
            clear_screen()
            print("🎉 Congratulations! You’ve guessed the word:", secret)
            break

        # 2.7) Check for loss
        if has_lost(wrong_guesses, max_lives):
            clear_screen()
            print(show_gallows(len(wrong_guesses), max_lives))
            print("💀 Game over! The word was:", secret)
            break

    # 3) End of game
    print("\nThanks for playing Hangman!")

if __name__ == "__main__":
    main()



