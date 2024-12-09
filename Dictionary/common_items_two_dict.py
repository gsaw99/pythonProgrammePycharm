dict1 = {'gfg': 1, 'is': 2, 'best': 3}
dict2 = {'gfg': 1, 'is': 2, 'good': 3}
common_keys = []
for key in dict1:
    if key in dict2:
        common_keys.append(key)
print(common_keys)

