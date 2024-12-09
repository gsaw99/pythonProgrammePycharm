class Father:

    def __init__(self, money):
        self.money = money
        print("Father class constructor")
    def show(self):
        print("Father class")

class Son(Father):
    def __init__(self, money, job):
        super().__init__(money)
        self.job = job
        print("Son class constructor")
    def display(self):
        print("Son class Method", self.money, self.job)
s = Son(1000, 'python')
s.show()
s.display()
