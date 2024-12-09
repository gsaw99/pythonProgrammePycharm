# Leap year> 366 days & come in 4 years
year = int(input("Enter a number of year here: "))

if year % 4 == 0 and year % 100 != 0:
    print("This is a Leap Year")

elif year % 400 == 0 and year % 100 == 0:
    print("This is a Leap Year")

else:
    print("This is not a leap year")