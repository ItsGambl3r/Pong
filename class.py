from abc import ABC, abstractclassmethod
class Instrument(ABC):
    __count = 0
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        Instrument.__count += 1

    @abstractclassmethod
    def play(self):
        pass
    
    def getName(self):
        return self.__name
    
    def getPrice(self):
        return self.__price

    @staticmethod
    def getCount():
        return Instrument.__count
    
    def __str__(self):
        return f"{self.__name} costs {self.__price}"
    
    def __eq__(self, other):
        return self.__name == other.__name and self.__price == other.__price
    
class Piano(Instrument):
    def __init__(self, name, color, price):
        super().__init__(name, price)
        self.__color = color

    def play(self):
        return f"{self.getName()} is playing"


x = Instrument("guitar", 100)
