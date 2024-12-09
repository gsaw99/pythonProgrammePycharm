def decor1(func): # get_name()=func()we can put "get_name" function name as a parameter in bracket or we can can put local parameter also
    def inner():
        return func().upper()
    return inner
def decor2(func):
    def inner():
        return func().split()
    return inner

@decor2
@decor1
def get_name():
    name=input("Enter first name: ")
    sirname=input("Enter sirname: ")
    full_name=name+" "+sirname
    return full_name
print(get_name())