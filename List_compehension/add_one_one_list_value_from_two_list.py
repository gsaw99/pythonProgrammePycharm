# Method1
'''list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

result = [i + j for i, j in zip(list1, list2)]
print(result)  # [6, 8, 10, 12]'''

# Method1
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

result = [i + j for i, j in zip(list1, list2) if (i+j) % 2 == 0]
print(result)  # [6, 8, 10, 12]
