dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
dict2 = {"c": 3, "d": 4, "e": 5, "f": 6}
common_key = []
for key in dict1:
    if key in dict2:
        common_key.append(key)
print(common_key)