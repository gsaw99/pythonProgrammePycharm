# Method1
'''num = [10, 0, -1, 7, 8, 10, -67]
num.sort()
print(num)
print("second largest element is :", num[-2])'''

# Method2
'''list1 = [5, 6, 8, 22, 34, 45, 2, 67, 555, 44, 1, -1, 0]
mylist = [i for i in list1 if i != max(list1)]  #we need to correct here
print(min(mylist))'''


# Method3
num = [20, 10, 0, -1, 30, 7, 8, 10, -67]
largest = num[0]
second_largest = num[0]
for i in range(len(num)):
    if num[i] > largest:
        largest = num[i]

for i in range(len(num)):
    if num[i] > second_largest and num[i] != largest:
        second_largest = num[i]

print(second_largest)
