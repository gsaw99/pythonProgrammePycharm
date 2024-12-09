#Method1

'''num1 = 12
num2 = 16
num3 = 20

if num1 > num2 and num1 > num3:
    print("Largest number is", num1)
elif num2 > num1 and num2 > num3:
    print("Largest number is", num2)
else:
    print("Largest number is", num3)'''

#Method2

num1 = int(input("Enter a first number here: "))
num2 = int(input("Enter a second number here: "))
num3 = int(input("Enter a third number here: "))

if num1 > num2 and num1 > num3:
    print("Largest number is:", num1)
elif num2 > num1 and num2 > num3:
    print("Largest number is: ", num2)
else:
    print("Largest number is:", num3)


