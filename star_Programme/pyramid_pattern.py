'''num=int(input("Enter a number of rows here:"))
for i in range(0,num+1):
    for j in range(0,num-i-1):
        print("",end=" ")

    for j in range(0,i+1):
        print("*",end=' ')

    print()'''


num = int(input("Enter a number of rows here:"))
for i in range(1, num+1):
    for j in range(num-i):
        print("", end=" ")

    for j in range(1, 2*i):
        print("*", end=' ')

    print()
