# Method1
dict1 = {"names": ["abc", "def", "xyz"], "locations": ["mumbai", "pune", "blore"]}
# output: {"names": ["ABC", "DEF", "XYZ"], "locations": ["Mumbai", "Pune", "Blore"]}
a = list(map(lambda x: x.upper(), dict1["names"]))
print(a)
