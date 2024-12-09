# Method1

'''i=1
while i<=5:
    j=1
    while j<=i:
        print('*',end='')
        j=j+1
    print()
    i=i+1'''

# Method2

num = int(input("Enter a number of rows here:"))
for i in range(1, num+1):
    for j in range(1, i+1):
        print("*", end='')

    print()
'''
*
**
***
****
*****'''



