num = int(input("Enter the number of rows here: "))
for i in range(0, num+1):
    for j in range(0, i+1):
        print(j+1, end=' ')

    print()