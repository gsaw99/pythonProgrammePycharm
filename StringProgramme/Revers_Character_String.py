# Method1

'''s = "Welcome Gopal"
rev = s[ ::-1]
print(rev)'''

# Method 2
'''s = "Welcome Gopal"
rev = reversed(s)  # this is reversed in built function
print(rev)
result = ''.join(rev)
print(result)'''

# Method3 reverse one by one word
'''s = "Welcome Gopal"
rev = reversed(s)
for ch in rev:
    print(ch)'''

# Method-4  do not use slicing,reverse function
s = "Welcome Gopal"
output = ''
i = len(s)-1  # 5-1=4,
while i >= 0:
    output = output+s[i]
    i = i-1  # length value should be decremented, ye loop while k under hi chalega ab jab
                    # tak ye length 0 na ho jaye
print(output)

# Method5, using comprehension
s = "altimetrick"
rev = "".join([s[i]for i in range(len(s)-1, -1, -1)])
print(rev)

# Method6
'''s = "Welcome Gopal"
l = len(s)-1 # 5-1=4,
for i in range(l,-1,-1):
    print(s[i], end="")'''