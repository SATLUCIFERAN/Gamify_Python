
words = input("Type any words: ").split()
if all(word.isalpha() for word in words):
    print("All words are letters only.")

'''
Type any words: Anakin Skywalker
All words are letters only.

'''