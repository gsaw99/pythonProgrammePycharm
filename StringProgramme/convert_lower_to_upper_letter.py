s = "Welcome To Gopal"
output = ""
for i in s:
    if i.isupper():
        output = output + i.lower()
    else:
        output = output + i
print(output)