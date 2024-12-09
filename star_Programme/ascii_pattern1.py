n = int(input("Enter the number of rows here: "))
for i in range(65, n+65):
    for j in range(65, i+1):
        print(chr(i), end=' ')

    print()

''' o/p
A 
B B 
C C C 
D D D D 
E E E E E 
F F F F F F '''
