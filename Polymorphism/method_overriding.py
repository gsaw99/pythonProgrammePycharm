# Redefine the parent class method in the child class method, called method overriding.
# Parent class ke behaviour ko child class ma change karna hi method overriding hota hai.(addition to multiplication)
# Without inheritance, it is not possible.


# Example1
'''class World:
    def displayinfo(self): # Parent claass method
        print("Welcome to the world")

class India:
    def displayinfo(self): # override the parent class method
        print("Welcome to India")

ind=India()
ind.displayinfo()'''  # o/p:Welcome to India

# if we want parent class method in output then we need to use super() class method below subclass method
'''class World:

    def show(self): # Parent claass method
        print("Welcome to the world")

class India(World):

    def show(self):
        super().show()  # super() keyword.child class method name
        print("Welcome to India")

obj=India()
obj.show()'''


#Example3
class Add:
    def result(self,a,b):
        print("Addition", a+b)

class Multi(Add): # without inheritance we can not make method overriding, we need two class
    def result(self,a,b):
        super().result(a,b) # if argument available in method bracket then we need to put same argument in super class
        print("Multiplication", a*b)

m1=Multi()
m1.result(5,6)



