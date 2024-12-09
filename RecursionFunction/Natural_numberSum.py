def natural(n):
    if n<=1:
        return n
    else:
        return n+natural(n-1)

n=int(input("Enter the number: "))
print(natural(n))