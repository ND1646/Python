with open("source.txt", "r") as source, open("destination.txt", "w") as dest:
    content = source.read()
    dest.write(content)
print("Content copied successfully!")
