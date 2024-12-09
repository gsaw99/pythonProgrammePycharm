list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

res = [value for i in list1 for value in i]

print(res)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]