with open("file.txt", "r") as file:
    lines = file.readlines()
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = sum(len(line) for line in lines)

print("Lines:", num_lines)
print("Words:", num_words)
print("Characters:", num_chars)
