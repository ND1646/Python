rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=' ')
    print()


rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print(chr(65 + j), end=' ')
    print()


rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=' ')
    print()


