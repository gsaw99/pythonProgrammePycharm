def even(start, n):
    list1 = []
    for i in range(start, start+2*n):
        if i % 2 == 0:
            list1.append(i)
    return list1
    return []


start = int(input("Enter the start value here:"))
n = int(input("Enter the number value here:"))
result = even(start, n)
print(result)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]