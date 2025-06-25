#write in file
name=input('enter your college name: ')
f=open("data.txt",'w')
f.write(name)
f.close()

#read in file
f=open("data.txt",'r')
print(f.read())
f.close()

#write content to our file
f=open("data.txt",'a')
f.write("\n this is your python programming.....!!!!!!")
f.close()
print("your data is added....")







