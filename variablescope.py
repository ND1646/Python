#global scope
a=20
def myfunc():
    #global a
    a=10
    print(a)
myfunc()
print(a)

#enclosed scope
def outer_func():
    x=30
    def inner_func():
        #nonlocal x
        x=5
        y=40
        print(x) #enclosing scope
        print(y)
        inner_func()
        print(x)
        outer_func()
        #print(x)
            
        
