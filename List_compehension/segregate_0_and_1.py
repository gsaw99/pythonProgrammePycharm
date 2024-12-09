list1 = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
#Output :  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
result = ([i for i in list1 if i == 0] + [i for i in list1 if i == 1])
print(result)  # [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]