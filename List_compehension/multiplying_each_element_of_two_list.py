list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

result = [i * j for i in list1 for j in list2]
print(result)  # [5, 6, 7, 8, 10, 12, 14, 16, 15, 18, 21, 24, 20, 24, 28, 32]