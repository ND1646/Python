#function declaration
def my_func():
    print("hello from function")
my_func()

#local variable
def my_local():
    a=10
    b=20
    print("variable a=",a)
    print("variable b=",b)
    return a+b
print(my_local())

#global variable
name="MJKACC"
grno=2362
def my_global():
    print("name :",name)
    print("grno :",grno)
my_global()
