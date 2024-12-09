# using by super class

class Add:

    def result(self, a, b):  # same function name and parametrers
        print("Addition is:", a+b)

class Multi(Add):

    def result(self, a, b):
        super().result(a, b) # a, b ke place pe apna value bhi de sakte ho, othewise ye jo object ma define kiya hun wo lega
        print("Multiplication is:", a*b) # # same function name and parametrers

obj1 = Multi()
obj1.result(5, 7) # ouput is : Multiplication is: 35, parent class ka method overide ho gaya
