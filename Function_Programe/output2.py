x = 9

def myfunc():
    x = x+1 # local scope variable
    print("python is "+ x) # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
myfunc()
 # outside function