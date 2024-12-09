s = "Altimetric123"
vowels = "aeiou"
v = 0
c = 0
u = 0
l = 0
for i in s:
    if i.isalpha():
        if i.lower() in vowels:
            v = v+1
        else:
            c = c+1
    if i.isupper():
        u = u+1
    if i.islower():
        l = l+1
print("vowel is:", v)
print("consonant is:", c)
print("upper letter is:", u)
print("lower letter:", l)
