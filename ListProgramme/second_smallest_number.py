# Method1 using by list comprehension

list1 = [5, 6, 8, 22, 34, 45, 2, 67, 555, 44, 1, -1, 0]
mylist = [i for i in list1 if i != min(list1)]
print(min(mylist))

# Method
'''num = [20, 10, 0, -1, 30, 7, 8, 10, -67]
smallest = num[0]
second_smallest = num[0]
for i in range(len(num)):
    if num[i] < smallest:
        smallest = num[i]

for i in range(len(num)):
    if num[i] < second_smallest and num[i] != smallest:
        second_smallest = num[i]

print(second_smallest)'''
