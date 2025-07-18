class animal:
    def __init__(self):
        self.dog()

    def cat(self):
        print("hey i am cat!!")
        self.dog()

    def dog(self):
        print("hey i am dog!!")

obj = animal()
obj.cat()

print("using getter and setter method")
class stud:
    def __init__(self):
        self._name = ""

    def getname(self):
        return self._name

    def setname(self, name):  # Corrected parameter
        self._name = name     # Corrected assignment

obj = stud()                 # Corrected object creation
obj.setname("mjkacc")        # Set name
name = obj.getname()         # Get name
print(name)

