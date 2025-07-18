#tail recursion
print("tail recursion")
def solve(n):
    if n==0:
        return
    print(n)
    solve(n-1)
solve(3)


#head recursion
print("head recursion")
def solve(n):
    if n==0:
        return
    print(n)
    solve(n-1)
solve(3)


#tree recursion
print("tree recursion")
def solve(n):
    if n==0:
        return
    print(n)
    solve(n-1)
solve(3)
