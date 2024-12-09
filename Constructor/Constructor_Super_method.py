class Father:

    def __init__(self):
        print("Father class constructor")

    def show(self):
        print("Father class")

class Son(Father):

    def __init__(self):
        super().__init__()
        print("Son class constructor")

    def display(self):
        print("Son class")
s = Son()
s.show()
s.display()
