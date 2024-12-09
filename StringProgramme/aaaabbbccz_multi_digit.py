# Method1
'''s = 'aaaabbbccz'
previous = s[0] # s[0] means=a
output = ''
count=1 # ye count karega kitna baar hai a,b,c,z ko
i=1
#for i in range(len(s)):
while i<len(s):
    if s[i] == previous: # Agar previous character same hai tabhi coubt hoga, otherwise else ma jayega
        count = count+1
    else:
        output = output+str(count)+previous
        previous = s[i]
        count = 1
    if i == len(s)-1: # This is for last character Z, otherwise z will not print
        output=output+str(count)+previous
    i = i+1

print(output)'''


# Method2
s = 'aaaabbbccz'
d = {}
for i in s:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1
print(d)
for i in d:
    print(i, d[i], end='')


