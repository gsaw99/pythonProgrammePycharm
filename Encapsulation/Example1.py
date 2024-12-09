#Method1
# Encapsulation helps to:
# Protect data: Prevent unauthorized access, accidental modification, and misuse of data
# In Python, encapsulation is achieved through conventions and programming practices, such as:
# Access modifiers: Use access modifiers like public, private, and protected to control the visibility of data and methods:
# Private members: Denote private data members with a double underscore prefix before their name. Only accessible within the class.
# Protected members: Denote protected data members with a single underscore prefix before their name. Accessible within the class and its subclasses.
# Property decorators: Use property decorators to achieve encapsulation.
class Parent:

    def __init__(self, java, python):
        self.java = java
        self.__python = python
    def show(self):
        print("Language")


class Child(Parent):
    def __init__(self):
        super().__init__('java', 'python')
        print("we will call the parent class member")

c = Child()
c.show()
c.java









'''class Mobile:

    def __init__(self):
        self.__price = 9000

    def sell(self):
        print("Selling Price",self.__price)

    def setPrice(self, price):
        self.__price = price

c = Mobile()
c.sell()
c.setPrice(10000)
c.sell()'''