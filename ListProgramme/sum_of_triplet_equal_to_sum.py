list1 = [1, 4, 45, 6, 10, 8]
sum_of_triple = 22
res = []
n = len(list1)
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if list1[i] + list1[j] + list1[k] == sum_of_triple:
               res.append((list1[i], list1[j], list1[k]))
print(res)