n = int(input("Enter the number of rows here: "))
for i in range(65, n+65):
    for j in range(65, i+1):
        print(chr(j), end=' ')

    print()

'''o/p:
A 
A B 
A B C 
A B C D 
A B C D E '''
