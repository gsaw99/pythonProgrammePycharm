#keys=input("Enter the keys here: ")
#values=input("Enter the values here: ")
# Converts list to dictionary
'''list1 = ['Gopal', 'mobileno', 'address']
list2 = [1, 2, 3]
result = dict(zip(list1, list2))
print(result)'''

# Method2
list1 = ['Gopal', 'mobileno', 'address']
list2 = [1, 2, 3]
d = {}
for key in list1:
    for value in list2:
        d[key] = value
        list2.remove(value)
        break
print(d)  # {'Gopal': 1, 'mobileno': 2, 'address': 3}
