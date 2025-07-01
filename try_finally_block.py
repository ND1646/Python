def func1():
    try:
        list=[1,3,5,7,9]
        i=int(input("enter the index number: "))
        print("your indexing value is: ",list[i])
        return 1
    except:
        print("some error occured.....!!!!!")
        return 0
    finally:
        print("i am always executed....")
x=func1()
print(x)
