str = input("Enter the strings here: ")
li = str.split()
dict = {}
print(li)
for i in li:
    if i in dict:
        dict[i] = dict[i]+1
    else:
        dict[i] = 1
print(dict)