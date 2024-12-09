def decor(addition):
    def inner():
        result = addition()  # Existing functionality
        num3 = int(input("Enter a third number: ")) # Add new functionality
        result = result+num3
        return result
    return inner

@decor
def addition():  # Now we need to modify the result or this function without disturbed it,
                   # means need to use decorators, need to add 3rd number also

    num1 = int(input("Enter a first number: "))
    num2 = int(input("Enter a second number: "))
    result = num1+num2
    return result
print(addition())