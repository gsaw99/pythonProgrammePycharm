class Factory:

    def __init__(self, BT, tyres, ET):
        self.BT = BT
        self.tyres = 4
        self.ET = ET

    def showdetails(self):
        print(f"your details are\n{self.BT},{self.tyres},{self.ET}")  # Format string

ferrari = Factory("covered", 4 ,"8 cycle")
alto = Factory("covered", 4, "4 cycle")
print(ferrari.tyres)
print(ferrari.BT)
print(ferrari.ET)
print(alto.tyres)
alto.showdetails()


