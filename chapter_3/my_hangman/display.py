
# display.py

def show_word_progress(secret, guesses):
    """
    Build and return a string like "P _ _ _ O _"
    where each letter in secret is shown if in guesses, else "_".
    """
    display_chars = [
        letter if letter in guesses else "_"
        for letter in secret
    ]

    return " ".join(display_chars)


def show_used_letters(guesses):
  
    return ", ".join(sorted(guesses))


GALLOWS = [
    # index 0: no wrong guesses yet
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    # index 1: head
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    # index 2: head + body
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    # index 3: one arm
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    # index 4: both arms
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    # index 5: one leg
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    # index 6: both legs (game over)
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
]


def show_gallows(wrong_guesses, max_lives=6):
    """
    Return the ASCII gallows art corresponding to the number of wrong guesses.
    Caps at max_lives.
    """
    index = min(wrong_guesses, max_lives)
    return GALLOWS[index]
