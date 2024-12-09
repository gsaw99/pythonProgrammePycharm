# Class is a blueprint for creating objects.
# Object is instances of class.
# provide security for data is called encapsulation
# Polymorphism means having many forms. Polymorphism-Ability to take various forms eg:-mobile phone taking
# photo,calculator, calendar
# Inheritance- when one class inherits some features from another class is called inheritance.
# Abstraction:-when we see only essential part of our code and hide the rest part is called abstraction.
# Self keyword is mandatory for calling variables name  into method
# className should be start from capital(First letter) like Factory, Student
class Calculator:
    num = 100  # Class variable(static variable)

    def __init__(self, a, b):  # self keyword current object ko refer karta hai,
                               # iske bina hamlog access nahi kar sakte class variable ko
        self.firstNumber = a  # instance variable(firstNumber) ,ye hamesha constructor ke under hi declare hoga
        self.secondNumber = b  # instance variable(firstNumber)
        print("I am called automatically when object is created")

    def getData(self):
        print("I am executing my code")

    def summation(self):
        return self.firstNumber+self.secondNumber+Calculator.num # Hamlog self.num bhi likh sakte hain or Class name se bhi likh sakte hain.

obj = Calculator(5, 2)
obj.getData()
print(obj.summation())
#print(Calculator.num) # Hamlog class variable ko classNmae or object reference ke through access kar sakte hain
obj1 = Calculator(7, 4)
obj1.getData()
print(obj1.summation())