## Public class
class car():
    def __init__(self, windows, doors, enginetype):
        self.windows = windows
        self.doors = doors
        self.engine = enginetype

# Protected class
class car():
    def __init__(self, windows, doors, enginetype):
        self._windows = windows
        self._doors = doors
        self._engine = enginetype

class Truck(car):
    def __init__(self, windows, doors, enginetype, horsepower):
        super().__init__(windows, doors, enginetype)
        self.horsepower = horsepower

truck =  Truck(4,5,"Diesel", 4000)

# private class
class car():
    def __init__(self, windows, doors, enginetype):
        self.__windows = windows
        self.__doors = doors
        self.__engine = enginetype

audi = car(4,4,"Diesel")
audi.__car__doors = 5
