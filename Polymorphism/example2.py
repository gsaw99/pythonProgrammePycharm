# Different classes with the same method
class Car:
   def __init__(self, brand, model):
     self.brand = brand
     self.model = model
   def move(self):
       print("Drive!")
class Boat:
   def __init__(self, brand, model):
     self.brand = brand
     self.model = model
   def move(self):
     print("Sail!")
class Plane:
   def __init__(self, brand, model):
     self.brand = brand
     self.model = model
   def move(self):
     print("Fly!")

car1 = Car("Ford", "Eco sports")       #Create a Car object
print(car1.brand,car1.model)
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
print(boat1.brand,boat1.model)
plane1 = Plane("Boeing", "747")     #Create a Plane object
print(plane1.brand,plane1.model)
for x in (car1, boat1, plane1):
  x.move()