def decor(sub):

    def inner():
        result = sub()
        num3 = int(input("Enter a num3 here:"))
        result = result - num3
        return result
    return inner

@decor
def sub():

    num1 = int(input("Enter a num1 here:"))
    num2 = int(input("Enter a num2 here:"))
    result = num1 - num2
    return result
print(sub())