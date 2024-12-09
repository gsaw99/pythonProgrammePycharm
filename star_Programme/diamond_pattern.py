# Method1
'''num=int(input("Enter a number of rows here:"))
for i in range(1,num+1):
    for j in range(1,num-i-1):
        print("",end=" ")

    for j in range(1,i+1):
        print("*",end=' ')

    print()
for i in range(1,num-1):
    for j in range(1,i+1):
        print("",end=" ")

    for j in range(1, num-i-1):
        print("*",end=' ')

    print()'''

# Method2
num = int(input("Enter a number of rows here:"))
for i in range(1, num+1):
    for j in range(num-i):
        print("", end=" ")

    for j in range(1, 2*i):
        print("*", end=' ')

    print()

#num=int(input("Enter a number of rows here:"))
for i in range(num+1, 0, -1):

        for j in range(num - i, 0, -1): # Inner loop for leading spaces in each row
            print(" ", end="")

        for k in range(2*i-1, 0, -1): # Inner loop for printing asterisks in each row
            print("*", end=" ")

        print() # Move to the next line after each row

