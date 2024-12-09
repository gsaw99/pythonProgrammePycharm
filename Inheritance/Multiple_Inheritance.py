class Father:

    def money(self):
        print("This is Father money")

class Mother:

    def food(self):
        print("This is Mother food")

class Child(Father, Mother):
    pass

obj = Child()
obj.money()
obj.food() # taking properties from both parents(mother and father ka)
