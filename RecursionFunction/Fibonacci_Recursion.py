def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return (fibo(n-2)+fibo(n-1))


n=int(input("Enter the number here:"))
print(fibo(n))

