import functools

lis = [1, 3, 5, 6, 2]
max1 = functools.reduce(lambda a, b: a if a > b else b, lis)
print(max1)