# {key:value for item in iterable if condition}
# eg1
'''dict1 = {i:i for i in range(15) if i % 2 == 0}
dict2 = {i:i*i for i in range(15) if i % 2 == 0}
print(dict1)
print(dict2)'''

# eg2
list1 = [1, 2, 3, 4, 5]
dict1 = {x: x**2 for x in list1}
print(dict1)