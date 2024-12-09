# Method1

'''list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
set1 = set(list1)
print(set1)
set2 = set(list2)
print(set1 & set2)'''

# Method2
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
list3 = []
for i in list1:
    if i in list2:
        list3.append(i)
print(list3)