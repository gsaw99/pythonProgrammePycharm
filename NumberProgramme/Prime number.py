# jis number ka factors only 2 hota hai wo prime hota hai
# or 2 numbers se jada ka factor composite number hota hai
# Method1: Input from user, Prime number always start from 2 and it should have always two factor.

lower = int(input("Please, Enter the Lowest Range Value: "))
upper = int(input("Please, Enter the Upper Range Value: "))

print("The Prime Numbers in the range are: ")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
         print(num)
        #Method2:
'''num = 11

for i in range(2, num):
    if num % i == 0:
        print("This is not a Prime number")
        break
else:
    print("Prime number")'''