list1 = [1, 1, 2, 3, 5, 6, 4, 4, 5, 7, 2, 3, 7, 7]
d = {}
for i in list1:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1
print(d)
