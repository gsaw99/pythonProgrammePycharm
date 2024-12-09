def creater1():
    num = int(input("Enter the number:"))
    i = 1
    while i <= num:
        yield i
        i = i+1

y = creater1()
print(next(y))
print(next(y))
