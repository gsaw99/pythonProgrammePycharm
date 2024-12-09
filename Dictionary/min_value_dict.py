# Method1

'''Input = {'Audi':100, 'BMW':1292, 'Jaguar': 210000, 'Hyundai' : 88}

Key_min = min(zip(Input.keys(), Input.values()))[1] # This is for value,[0] means key ayega, [1] means value ayega
print(Key_min)'''

# Method2
d = {'Audi': 100, 'BMW': 1292, 'Jaguar': 210000, 'Hyundai': 88}
list1 = list(d.items())
print(list1)
largest = list1[0]
for i in range(len(list1)):
    if list1[i] < largest:
        largest = list1[i]
print(largest)