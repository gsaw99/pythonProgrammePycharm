P = int(input("Enter a number:"))
R = int(input("Enter a number of Rate:"))
T = int(input("Enter a number of times:"))
A = P * (pow((1 + R / 100), T))
print("Result of Amount:", A)
CI = A - P
print("Result of Compound interest:", CI)