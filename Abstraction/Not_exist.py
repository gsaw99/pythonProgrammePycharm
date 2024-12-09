# Abstraction is not exist in python

from abc import ABC , abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius=radius

    def area(self): #area and perimeter wala method ko yahan likhna hoga otherwise error ayega, q
                       #ki ye absract hai otherwise ye ayega-->> TypeError: Can't instantiate abstract
                       #class Circle with abstract methods area, perimeter
            pass

    def perimeter(self):
            pass

cir1=Circle(4)
#print(cir1.area())



