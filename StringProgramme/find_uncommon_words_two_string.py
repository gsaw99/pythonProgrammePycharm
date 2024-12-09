s1 = "Geeks for Geeks done"
s2 = "Learning from Geeks for Geeks"
str1 = s1.split()
str2 = s2.split()
str3 = []
for i in str1:
    if i not in str2:
        str3.append(i)
for i in str2:
    if i not in str1:
        str3.append(i)
print(str3)  # ['Learning', 'from']