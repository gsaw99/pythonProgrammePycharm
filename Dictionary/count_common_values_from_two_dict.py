dict1 = {'gfg': 1, 'is': 2, 'best': 3}
dict2 = {'gfg': 1, 'is': 2, 'good': 3}
# Using dictionary comprehension
res = {key: dict1[key] for key in dict1 if key in dict2 and dict1[key] == dict2[key]}
print(res)
print(len(res))