# Method1
'''num = [10, 0, -1, 7, 8, 10, -67]
min_num=min(num)
print(min_num)'''

# Method2
num = [10, 0, -1, 7, 8, 10, -67]
min_number = num[0]
for i in range(len(num)):
    if num[i] < min_number:
        min_number = num[i]
print(min_number)