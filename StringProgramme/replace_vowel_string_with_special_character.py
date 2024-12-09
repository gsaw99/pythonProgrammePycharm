str1 = "Gopal"
vowel = "aeiou"
for i in str1:
    if i.lower() in vowel:
        print("%", end="")
    else:
        print(i, end="")