# Write a program to print the characters present at even index and odd index seperately for the
# given string
#Method1
# s = input("Enter a string here: ")
s = "Gopalkumarsaw"
print("characters at even index")
i = 0
while i < len(s):
    print(s[i])

    i = i+2
print("characters at odd index")
i = 1
while i < len(s):
    print(s[i])
    i = i+2

#Method2
'''s = input("Enter a string here: ")
print("characters at even index")
l = s[0::2]
print(l)
print("characters at odd index")
l = s[1::2]
print(l)'''

# Method3
'''s="GopalSoftwareSolution"
result=s.replace(""," ")
print(result)
str1=result.split()
print(str1)
for i in range(len(str1)):
    if i%2==0:
        print("Even string", str1[i])
    else:
        print("Odd string", str1[i])'''



