# A variable declared outside of the function or scope is called global variable.
# A global variable is also used in outside or inside of the function or calss


x='awesome' # global scope variable

def myfunc():
    global x # made global variable, ab fantastic print hoga q ki X global ban gaya hai
    x='fantastic' # local scope variable

myfunc()
print("python is " + x) # o/p:- python is fantastic, outside function