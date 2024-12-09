class Human_being:

    def __init__(self):
        print("human being constructor called")
        self.name = input("Enter your name:")

class Employee(Human_being):

    def __init__(self):
        print("Employee constructor called")
        self.salary = int(input("Enter your salary:"))

class Manager(Employee):

    def __init__(self):
        print("Manager constructor called")
        self.bonus = int(input("Enter your bonus:"))
m1=Manager()
