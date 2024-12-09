num = [10, 5, 4, 20, 40, 50, 3]
largest_number = num[0]
second_largest_number = num[0]
third_largest_number = num[0]
for i in range(len(num)):
    if num[i] > largest_number:
        largest_number = num[i]

for i in range(len(num)):
    if num[i] > second_largest_number and num[i] != largest_number:
        second_largest_number = num[i]
#print(second_largest_number)

for i in range(len(num)):
    if num[i] > third_largest_number and num[i] != second_largest_number and num[i] != largest_number:
        third_largest_number = num[i]
print(third_largest_number)