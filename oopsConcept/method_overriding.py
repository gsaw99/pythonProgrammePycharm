# Method overriding ma parent and child class ke pass same name ka method name rahega, same parameters bhi rahega.
# but child class parent class ke method ko override kar deta hai.
# without inheritence it is not posssible
# memory reduce bhi hota hai isse
# Agar apko parent class ka bhi method chaiye to super() class method ke saath ma parent class method ko
# dot(.) add karna hoga with parameters value use karna padega child class method ke just niche ma

class Add:

    def result(self, a, b):  # same function name and parametrers
        print("Addition is:", a+b)

class Multi(Add):

    def result(self, a, b):
        print("Multiplication is:", a*b) # # same function name and parametrers

obj1 = Multi()
obj1.result(5, 7) # ouput is : Multiplication is: 35, parent class ka method overide ho gaya
