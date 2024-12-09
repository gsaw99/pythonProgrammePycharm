# Method1
'''num = [10, 0, -1, 7, 8, 10, -67]
num.sort()
print(num)'''

# Method1, using FOR Loop
num = [10, 0, -1, 7, 8, 10, -67]
for i in range(0, len(num)):
    for j in range(i+1, len(num)):
        if num[i] >= num[j]:
            num[i], num[j] = num[j], num[i]
print(num)  # [-67, -1, 0, 7, 8, 10, 10] sorted in ascending order

