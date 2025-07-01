a=input("Enter the number:")
print(f"multiplication table of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)}*{i}={int(a)*i}")            
except:
    print("invalid input.....!!!!!")
