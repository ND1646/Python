from collections import Counter

with open("file.txt", "r") as file:
    content = file.read()
    frequency = Counter(content)

print("Character Frequency:\n", dict(frequency))
