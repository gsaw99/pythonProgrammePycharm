# Method1
'''list1 = [[1, 2], [3, 4], [5, 6]]
list2 = [[3, 4], [5, 7], [1, 2]]
list3 = []
for i in list1:
    if i not in list2:
        list3.append(i)
for i in list2:
    if i not in list1:
        list3.append(i)
print(list3)  # [[5, 6], [5, 7]]'''

# Method2, list comprehension
list1 = [[1, 2], [3, 4], [5, 6]]
list2 = [[3, 4], [5, 7], [1, 2]]
res_list = [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]
print(res_list)  # [[5, 6], [5, 7]]

