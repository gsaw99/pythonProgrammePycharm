# Write a program for the following requirement
#input:a4b3c2
#output:aaaabbbcc means a 4 times,b 3 times, c 2 times
s = 'a4b3c2'
output = ''
for ch in s:
    if ch.isalpha():  # True
        x = ch  # x=a
    else:
        d = int(ch) # Yahan pe type casting karna hoga otherwise ye multiply nahi karega ki ye kitna time hai,
                  # string and string multiply nahi hota hai.
        output = output+x*d # yahan pe multiply hoga ki a,b,c kitna baar hai
print(output)