# Method1
'''list1 = [2, 2, 3, 4, 5, 3, 4, 6, 7, 8, 9]
for i in list1:
    if list1.count(i) > 1:
        print(i, end=" ")'''

# Method3
'''list1 = [2, 2, 3, 4, 5, 3, 4, 6, 7, 8, 9]
for i in range(0, len(list1)):
    for j in range(i+1, len(list1)):
        if list1[i] == list1[j]:
            print(list1[j])'''

# Method2
list1 = [2, 2, 3, 4, 5, 3, 4, 6, 7, 8, 9, 9]
unique = []
duplicate = []
for i in list1:
    if i not in unique:
        unique.append(i)
    else:
        duplicate.append(i)
print(duplicate)

#Method3




