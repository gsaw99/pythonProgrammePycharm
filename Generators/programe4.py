def show(a, b):

    while a <= b:
        yield a
        a=a+1
result=show(1,6)
print(next(result))
print(next(result))
print(next(result))
print(next(result))

