from abc import ABC
class car(ABC):
    def mileage(self):
        pass
class tesla(car):
    def mileage(self):
        print("the mileage is 30kmph")
class suzuki(car):
    def mileage(self):
        print("the mileage is 25kmph")
t=tesla()
t.mileage()
s=suzuki()
s.mileage()
