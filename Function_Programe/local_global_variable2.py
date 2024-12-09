x = 5

def hello():
    global a
    a="this is a global variable"
    x = 10
    print(a)
    print("local x:", x)
hello()
print("global x: ", x)
print(a)
