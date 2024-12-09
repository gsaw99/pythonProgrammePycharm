# Method1
'''num = [10, 0, -1, 7, 8, 10, -67]
print(max(num))
max_num=max(num)
print(max_num) # 10'''

# Method2, using by for loop
num = [10, 0, -1, 7, 8, 10, -67]
largest_number = num[0]
for i in range(len(num)):
    if num[i] > largest_number:
       largest_number = num[i]
print(largest_number)