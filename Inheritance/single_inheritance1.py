class Parent:
    def money(self):
        print("This is Parent money")

class Child(Parent):
    pass

obj = Child()
obj.money()
