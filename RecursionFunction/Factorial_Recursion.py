# Method1
'''def fact(n):
    if n==0:
        return 1
    return n*fact(n-1) # n=5, 5*fact(5-1)=5*4=20,

print(fact(10))'''

#Method2
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1) # n=5, 5*fact(5-1)=5*4=20,
x=int(input("Enter a number here:"))
print(fact(x))

