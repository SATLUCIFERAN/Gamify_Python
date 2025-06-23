

words = ["Python", "makes", "string", "joining", "easy"]
sentence = " ".join(words)
print(sentence)

# Python makes string joining easy


fields = ["Alice", "Bob", "Charlie"]
line = ",".join(fields)
print(line)

# Alice,Bob,Charlie


text = "red|green|blue"
colors = text.split("|")          
new_text = " & ".join(colors)

print(colors)               # ["red", "green", "blue"]
print(new_text)             # red & green & blue


nums = [1, 2, 3]
line = "-".join(str(n) for n in nums)
print(line)
# 1-2-3


