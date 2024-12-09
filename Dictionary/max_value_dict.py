# This is called in the interview
# Mehod1
'''Input = {'Audi':100, 'BMW':1292, 'Jaguar': 210000, 'Hyundai' : 88}

Key_max = max(zip(Input.keys(), Input.values()))[1] # This is for value and key just change index number
print(Key_max)'''

# Method2
d = {'Audi': 100, 'BMW': 1292, 'Jaguar': 210000, 'Hyundai': 88}
list1 = list(d.items())
print(list1)
largest = list1[0]
for i in range(len(list1)):
    if list1[i] > largest:
        largest = list1[i]
print(largest)

# Method3
'''d = [{'Audi': 100, 'BMW': 1292, 'Jaguar': 210000, 'Hyundai': 88}]
max_dict = {key: max(i[key] for i in d) for key in d[0].keys()}
print(max_dict)'''