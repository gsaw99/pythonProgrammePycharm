# By using while
'''n=int(input("Enter a number here:"))
i=2
sum1 = 0
while i<=n:
    sum1 = sum1+i
    i=i+2

print("sum of even numbers is :", sum1)'''

# Mwthod2, by using for
num = int(input("Enter a number here:"))
sum1 = 0
for i in range(2, num + 1, 2):
    sum1 = sum1 + i
print(sum1)
