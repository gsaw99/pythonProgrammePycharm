# Without Constructor
'''class Calculate:
    def sum(self,a,b):
        print(a+b)

class Number(Calculate):
    pass
obj=Number()
obj.sum(5,9)'''


# Using Constructor
class Hero:
    def __init__(self, reel_name, hero_name):
        self.reel_name = reel_name
        self.hero_name = hero_name
    def show(self):
        print(self.reel_name)
        print(self.hero_name)
class Name(Hero):
    def __init__(self, real_name, reel_name, hero_name):  # If we put constructor in both classes then parent constructor method will not come in output
        self.real_name = real_name
        self.reel_name = reel_name
        self.hero_name = hero_name

    def display(self):
        print(self.reel_name)
obj = Name("Rachit","Ajay","Gopal")
obj.display()
obj.show()













'''class Human_being:
    def __init__(self):
        print("human being constructor called")
        self.name=input("Enter your name:")

class Employee(Human_being):
    def __init__(self):
        print("Employee constructor called")
        self.salary=int(input("Enter your salary:"))
        print(self.salary)

e1=Employee()'''

