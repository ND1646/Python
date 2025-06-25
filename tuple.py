#CREATE EMPTY TUPLE
t1=()
print("Empty tuple:",t1)

t2=(1,2,3,4,5)
print("tuple with multiple value:",t2)

t3=2,3,4,5,6
print("tuple without parenthessis:",t3)

t4=[3,4,5,6,7]
print("tuple with lists:",t4)

t5=(1,2,3,4)*3
print("tuple with repetiton:",t5)

t6=tuple(range(6))
print("tuple from range:",t6)

tup=(1,4,8,8,8,8,8,"mjkacc",True)
print(type(tup),tup)
print(len(tup))
print(tup[3])
print(tup[2])
x=tup.index("mjkacc")
print(x)
y=tup.count(8)
print(y)








