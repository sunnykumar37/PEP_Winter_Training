# Class Methods and Class Variables

class Car:
    base_price = 100000 # class variable
    def __init__(self, windows, doors, power):
        self.windows =  windows
        self.doors = doors
        self.power = power

    def what_base_price(self):
        print("The base price is: {}".format(self.base_price))
    @classmethod
    def revise_base_price(cls, Inflation):
        cls.base_price = cls.base_price+cls.base_price*Inflation
    
Car.revise_base_price(0.10)

print(Car.base_price)
Car.revise_base_price(0.07)
car1 = Car(4,5,2000)
print(car1.base_price)