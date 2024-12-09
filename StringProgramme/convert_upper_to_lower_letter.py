# Method1
'''s = "Welcome to Gopal"
upper_letter = ""
for ch in s:
    if ch.islower():
        upper_letter = upper_letter+ch.upper()
    else:
        upper_letter = upper_letter+ch

print(upper_letter)'''

# Method2
s = "Welcome To Gopal"
upper_letter = ""
for i in s:
    if i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        upper_letter = upper_letter+i
    else:
        k = ord(i)  # change in number
        l = k+32  # k is a diference between A and a
        upper_letter = upper_letter+chr(l)
print(upper_letter)



