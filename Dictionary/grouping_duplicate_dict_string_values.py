# Method1
d = {1: "apple", 2: "apple", 3: "apple", 4: "banana", 5: "banana", 6: "banana", 7: "banana", 8:
     "cherry", 9: "cherry", 10: "apple"}
res = {}
for key, value in d.items():
    if value not in res:
        res[value] = [key]
    else:
        res[value].append(key)
print(res)  # {'apple': [1, 2, 3, 10], 'banana': [4, 5, 6, 7], 'cherry': [8, 9]}