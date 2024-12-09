# Operator overloading:-We can use same operator for multiple purposes,called operator overloading.
# eg: + operator used in string concatenation & Arithmetic addition
# print(10+20)
# print('durga'+'gopal')
# python supports
class example:
    def __init__(self, X):
        self.X = X

        # adding two objects

    def __add__(self, U):
        return self.X + U.X


object_1 = example(int(input(print("Please enter the value: "))))
object_2 = example(int(input(print("Please enter the value: "))))
print(": ", object_1 + object_2)
object_3 = example(str(input(print("Please enter the value: "))))
object_4 = example(str(input(print("Please enter the value: "))))
print(": ", object_3 + object_4)