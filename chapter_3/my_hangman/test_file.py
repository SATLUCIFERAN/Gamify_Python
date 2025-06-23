
from utils import load_wordlist
wl = load_wordlist()
print(wl[:5])

# ['PYTHON', 'HANGMAN', 'DEVELOPER', 'CODE', 'FUNCTION']


from utils import choose_secret

print(choose_secret(wl))

'FUNCTION'  # random word

print(choose_secret(wl))
'PYTHON'    # random word


secret = choose_secret(load_wordlist())
print(secret)

'HANGMAN'   # random word
