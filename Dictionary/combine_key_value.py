# Dictionary comprehension is a smart and simple way to create a new dictionary from python iterable.
# combine two dictionary key:value
# Method1
'''list1 = ['Name', 'age', 'roll_no', 'address', 'state', 'district']
list2 = ['Gopal', 32, 2, 'jharia', 'Jharkhand', 'Dhanbad']
list3 = dict(zip(list1, list2))
print(list3)'''

# Method2
list1 = ['Name', 'age', 'roll_no', 'address', 'state', 'district']
list2 = ['Gopal', 32, 2, 'jharia', 'Jharkhand', 'Dhanbad']
d = {}
for key in list1:
    for value in list2:
        d[key] = value
        list2.remove(value)
        break
print(d)

# using comprehension
'''list1 = ['Name', 'age', 'roll_no', 'address', 'state', 'district']
list2 = ['Gopal', 32, 2, 'jharia', 'Jharkhand', 'Dhanbad']

res = {list1[i]: list2[i] for i in range(len(list1))}
print(res)'''