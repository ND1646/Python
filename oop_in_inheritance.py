class Employee:
    def __init__(self, name, idnum):
        self.name = name
        self.idnum = idnum

    def showdetails(self):
        print(f"The name of employee {self.idnum} is {self.name}")

class Programmer(Employee):
    def showlanguage(self):
        print("The default language is Python")

# Creating objects properly
e1 = Programmer("Ramdas", 100)
e1.showdetails()


e2 = Programmer("Laxmandas", 101)
e2.showdetails()
e2.showlanguage()
