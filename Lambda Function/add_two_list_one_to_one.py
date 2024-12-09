# Returns a list of the results after applying the given function to each item of a given iterable
# Method1
'''list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list(map(lambda x, y: x + y, list1, list2))
print(result)'''
# Method2

list1 = [1, 2, 3]
list2 = [4, 5, 6]
i = 0
j = 0
output = []
while len(list1) > i or len(list2) > j:
    output.append(list1[i]+list2[j])
    i = i+1
    j = j+1
print(output)  # [5, 7, 9]

