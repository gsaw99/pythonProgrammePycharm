list1 = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 11, 14]
d = {}
for i in list1:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1
print(d)
