num = int(input("Enter a number: "))
order = len(str(num))
total = sum(int(d)**order for d in str(num))

if num == total:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
