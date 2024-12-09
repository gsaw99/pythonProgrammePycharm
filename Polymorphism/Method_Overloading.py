# Polymorphism-Ability to take various forms
# same method name with different task
# Same function with different arguments
# Method Overloading-if methods having same name but different type of arguments(last method will come in o/p)
# Does not support by python, The reason is as Python does not have a data type for method parameters.
# but we have a way.
class sumClass:

    def sum(self, a, b):
        print("First method:", a + b)

    def sum(self, a, b, c):
        print("Second method:", a + b + c)


obj = sumClass()
obj.sum(19, 8, 77)  # correct output
obj.sum(18, 20)  # throws error

'''
The previous function having the same name(but different parameters) gets overridden with the new function 
having the same name. So now, if we try to call the first function, which had different number parameters, 
by passing a different number of arguments defined in the new function, we get an error. 
Let us try to understand the same.
'''
'''In the above program, we can see that the second sum method overrides the first sum method. 
When we call the function using three arguments, it gives the output, but when we use two argument, 
it gives an error. Hence we can say that Python does not support function overloading.

But does that mean there is no other way to implement this feature? The answer is no. 
There are other ways by which we can implement function overloading in Python.

We can achieve it by setting one or more parameters as None in the function declaration. 
We will also include the checking condition for None in the function body so that while calling 
if we don't provide the argument for a parameter that we have set as None, an error won't occur.'''


'''class sumClass:
    def sum(self, a=None, b=None, c=None):
        if a != None and b == None or c == None:
            print("Provide more numbers")  # if there is only 1 number as input
        else:
            print("First method:", a + b + c)  # for calculating the sum


obj = sumClass()
obj.sum(19, 8, 77)  # 104
obj.sum(18)  # Provide more numbers'''


