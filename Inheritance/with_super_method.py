class Factory:

    def __init__(self, BT, tyres, ET):
        self.BT = BT
        self.tyres = tyres
        self.ET = ET

    def showdetails(self):
        print(f"your details are\n{self.BT},{self.tyres},{self.ET}") # Format string

class Honda(Factory):

    def __init__(self, BT, tyres, ET, glass):
        super().__init__(BT, tyres, ET)
        self.glass = glass

obj1 = Honda(1, 2, 3, 4)
print(obj1.showdetails())

