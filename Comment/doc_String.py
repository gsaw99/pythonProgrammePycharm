'''The strings enclosed in triple quotes that come immediately after the defined function are called Python docstring.
It's designed to link documentation developed for Python modules, methods, classes, and functions together.
It's placed just beneath the function, module, or class to explain what they perform.
The docstring is then readily accessible in Python using the __doc__ attribute.'''


def add(x, y):
    """This function adds the values of x and y"""
    return x + y


# Displaying the docstring of the add function
print(add.__doc__)