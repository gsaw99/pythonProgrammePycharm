def prime(n, i): # n=13, i=n-1=13-1=12
    if i==1:
        return 1
    if n%i==0:  # 20%10==0
        return 0
    return prime(n, i-1)
n=int(input("Enter the number here:"))

ind = prime(n, n-1)  # 13,13-1=12

if ind==1:
    print("prime number")
if ind==0:
    print("Not prime number")


