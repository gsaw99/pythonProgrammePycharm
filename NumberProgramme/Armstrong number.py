# number and sum of cube of their number should be same like 153=1 cube + 5 cube + 3 cube = 153
num = int(input("Enter a number here: "))  # 153
temp = num
sum = 0 # Initialization
while temp > 0:
    digit = temp % 10  # 153 % 10 = remainder is 3, 15%10=5, 1%10=1 hota hai
    cube = digit ** 3 # 3**3 = 27,5**3=125, 1**3=1
    sum = sum+cube  # 0+27=27, 27+125=152, 152+1=153

    temp = temp // 10  # 153//10=quotient is 15, 15//10= 1, 1//10=0.5 but
                       # will take 0 always before decimal value in floor division case


if num == sum:
    print("This is an ARMSTRONG number")
else:
    print("Not Armstrong number")




