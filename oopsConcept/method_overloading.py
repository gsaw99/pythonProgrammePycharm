class Area:

    def find_area(self, a=None, b=None):
        if a != None and b != None:
            print("Are of rectangle", a*b)
        elif a != None:
            print("Area of squre is:", a*a)
        else:
            print("Nothing print")
obj1 = Area()
obj1.find_area()
obj1.find_area(5)
obj1.find_area(3, 4)
