num = [5, 10, 6, 13, 19, 30, 20, 22]
even = 0
odd = 0
for i in num:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Total even number is=:", even)
print("Total odd number is=:", odd)