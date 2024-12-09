# Make your code more reusable
# Easier to work with large programs.
# oops programs prevent from repeating code
# oops provide security
# Class:- It is a blueprint of entities
# Object:- It is a instance of class
# Encapsulation:- Provide data scurity to make variable as private, protected.
# Inheritance
# Abstraction
# Polymorphism:- Same function but different behaviour
# static method:- Agar hamlog @staticmethod likh denge function ke upar to self likhne ka jarurat nahi hai,
# isko koi matlab nahi hai object ke instance se , ye sirf class ke liye work karta hai.
class Car:
    total_car = 0 # class variable

    def __init__(self, brand, model):
        self.__brand=brand # Private
        self.model=model # instance variable
        #self.total_car += 1 # hamlog class variable ko self and classname done se access kar sakte hain
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self): # Polymorphism example
        return "Petrol"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self): # Polymorphism example
        return "Electric charge"


my_tesla = ElectricCar("Tesla", "Model5", "85kwh")
#print(my_tesla.__brand)
#print(my_tesla.get_brand())
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())
print(Car.total_car)



