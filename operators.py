a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)


x = 5
y = 8

print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)
print("Greater or Equal:", x >= y)
print("Less or Equal:", x <= y)

num = 10
print("Original:", num)

num += 5
print("After += :", num)

num -= 2
print("After -= :", num)

num *= 3
print("After *= :", num)

num /= 4
print("After /= :", num)

num %= 3
print("After %= :", num)

num **= 2
print("After **= :", num)

num //= 2
print("After //= :", num)


a = True
b = False

print("AND:", a and b)
print("OR:", a or b)
print("NOT a:", not a)


x = 5       # 0101
y = 3       # 0011

print("AND:", x & y)   # 0001
print("OR:", x | y)    # 0111
print("XOR:", x ^ y)   # 0110
print("NOT x:", ~x)    # -(x+1)
print("Left Shift:", x << 1)  # 1010
print("Right Shift:", x >> 1) # 0010



age = int(input("Enter your age: "))

status = "Adult" if age >= 18 else "Minor"
print("Status:", status)



