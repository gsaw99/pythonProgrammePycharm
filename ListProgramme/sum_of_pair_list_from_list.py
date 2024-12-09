# Method1
#lst = [(4, 5), (6, 7), (3, 6), (1, 2), (1, 8)]
#k = 9
lst = [1, 5, 3, 7, 9]
k = 10
output = []
for i in range(len(lst)):
    for j in range(i, len(lst)):
        if (lst[i] + lst[j]) == k:
            output.append((lst[i], lst[j]))
print(output)
# Method2

'''from itertools import combinations

for var in combinations(lst, 2):
    if var[0] + var[1] == k:
        output.append((var[0], var[1]))
print(output)'''

# Method3
'''

while lst:
    num = lst.pop()
    diff = k - num
    if diff in lst:
        output.append((diff, num))

#output.reverse()
print(output) # [(1, 9), (3, 7)]'''

