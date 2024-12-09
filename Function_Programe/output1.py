x='awesome' # global scope variable

def myfunc():
    x='fantastic' # local scope variable
    print("python is "+ x)

myfunc()
print("python is " + x) # outside function