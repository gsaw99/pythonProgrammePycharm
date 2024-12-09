import functools
# using reduce to compute sum of list
lis = [1, 3, 5, 6, 2]
sum1 = functools.reduce(lambda a, b: a+b, lis)
print(sum1)
