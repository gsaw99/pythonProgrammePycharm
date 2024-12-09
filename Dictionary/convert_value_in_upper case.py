# Method1
'''
dict1 = {"names": ["abc", "def", "xyz"], "locations": ["mumbai", "pune", "blore"]}
# output = {"names": ["ABC", "DEF", "XYZ"], "locations": ["Mumbai", "Pune", "Blore"]}

res = {key: [val.upper() for val in value] for key, value in dict1.items()}

print(res)'''

# Method2
'''dict1 = {"names": ["abc", "def", "xyz"], "locations": ["mumbai", "pune", "blore"]}
res = list(map(lambda x:x.upper(), dict1["names"]))
print(res)'''

# Method3
dict1 = {"names": ["abc", "def", "xyz"], "locations": ["mumbai", "pune", "blore"]}
for key, value in dict1.items():
    for i in range(len(value)):
        value[i] = value[i].upper()
print(dict1)