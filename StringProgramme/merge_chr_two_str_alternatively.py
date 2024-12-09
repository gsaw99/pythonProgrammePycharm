# Write a program to merge character of two strings into a single string by taking character
# alternatively
str1 = input("Enter first string here:") # both string length should be same otherwise it can not the work but we can resolve this issue from method2
str2 = input("Enter second string here:")
i, j = 0, 0
output = ''
while i < len(str1) or j < len(str2):
    output = output+str1[i]+str2[j]
    i = i+1
    j = j+1
print(output)

#Method2
'''str1=input("Enter first string here:")  # extra character of string should come in last
str2=input("Enter second string here:")
i,j=0,0
output=''
while i<len(str1) or j<len(str2):
    if i<len(str1):
        output=output+str1[i]
        i=i+1
    if j<len(str2):
        output=output+str2[j]
        j=j+1
print(output)'''

# Method3

