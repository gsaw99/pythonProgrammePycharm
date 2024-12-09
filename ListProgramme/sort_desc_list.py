# Method1
'''num = [10, 0, -1, 7, 8, 12, -67]
num.sort(reverse=True)
print(num)'''

# Method1, using FOR Loop
num = [10, 0, -1, 7, 8, 12, -67]
for i in range(0, len(num)):
    for j in range(i+1, len(num)):
        if num[i] <= num[j]:
            num[i], num[j] = num[j], num[i]
print(num)# [12, 10, 8, 7, 0, -1, -67] sorted in descending order


