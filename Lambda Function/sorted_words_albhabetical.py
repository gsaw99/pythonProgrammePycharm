num = ['Jaipur', 'Goa',  'Kota', 'Dhanbad', 'Mumbai', 'Delhi' ]
for i in range(0, len(num)):
    for j in range(i+1, len(num)):
        if num[i] >= num[j]:
            num[i], num[j] = num[j], num[i]
print(num)  #  ['Delhi', 'Dhanbad', 'Goa', 'Jaipur', 'Kota', 'Mumbai']