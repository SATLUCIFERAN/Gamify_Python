
from logic import process_guess, has_won, has_lost

secret = "PYTHON"
correct = set()
wrong   = set()
max_lives = 6

# 1) Correct guess
process_guess(secret, "P", correct, wrong)
assert correct == {"P"} and wrong == set()

# 2) Wrong guess
process_guess(secret, "A", correct, wrong)
assert wrong == {"A"}

# 3) Winning condition
for letter in ["Y", "T", "H", "O", "N"]:
    process_guess(secret, letter, correct, wrong)
assert has_won(secret, correct) is True

# 4) Losing condition
wrong = {"A","B","C","D","E","F"}
assert has_lost(wrong, max_lives) is True

