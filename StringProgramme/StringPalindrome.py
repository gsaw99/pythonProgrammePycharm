# Method1
'''a = input("Enter a word here: ")  #
rev = a[ ::-1]
if a == rev:
    print("This is a String Palindrome")
else:
    print("This is not a String Palindrome")'''

# Method2
#s = "madam"
s = input("Enter a string here:")
output = ''
l = len(s)-1  # 5-1=4,
while l >= 0:
    output = output+s[l]
    l = l-1  # length value should be decremented, ye loop while k under hi chalega ab jab
                    # tak ye length 0 na ho jaye
print(output)
if s == output:
    print("Palindrome string")
else:
    print("Not Palindrome String")

