# 0,1,1,2,3,5,8,13 This is called fibonacci series(0+1=1, 1+1=2, 1+2=3 like that)
a = 0
b = 1
num = int(input("Enter a number: "))
for i in range(2, num+1):
    c = a+b
    a = b
    b = c
    print(c)
