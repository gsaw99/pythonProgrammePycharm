# 121=121 opposite number should be same

num = int(input("Enter a number here: "))
temp = num  # 121
rev = 0
while num > 0:  # 121>0
    digit = num % 10  # 121 % 10= 1, 12%10=2, 1%10=1
    rev = rev*10+digit  # 0*10+1=1, 1*10+2=12
    num = num//10  # 121/10= 12 quotient, 12/10=1
#print(rev) # just put here print for reverse any number
if temp == rev:
    print("This is a palindrome number")
else:
    print("This is not a palindrome number")

