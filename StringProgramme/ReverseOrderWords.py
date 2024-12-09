# Metod1
'''s = 'Learning python is very easy'
# output:- easy very is python Learning
l = s.split()  # it converts in list
print(l)
l1 = l[ ::-1]  # reverse the words
print(l1)
output = ' '.join(l1)# it will come without seperator
print(output)'''

# Method2
string = 'Learning python is very easy'
# output:- easy very is python Learning
s = string.split()  # it converts in list
i = len(s)-1
print(i)
l = []
print(s)
while i >= 0:
    l.append(s[i])
    i = i-1
print(l)
output = ' '.join(l)# it will come without seperator
print(output)

# Method3 , For Digits String

'''str1="10,58,192,67"
str2=str1.replace(",", " ")
print(str2)
spl=str2.split()
print(spl)
l=len(spl)-1
print(l)
output=[]
while l>=0:
    output.append(spl[l])
    l=l-1
print(output)
result=','.join(output)
print(result)'''

# Method4, using by FOR Loop

'''string = '192.298.10.67' # dot(.) ko pahle replace karna hoga space se, uske baad hi hoga ye
s=string.replace("."," ")
print(s)
spl=s.split()
output=[]
for i in range(len(spl)-1,-1,-1):
    output.append(spl[i])
print(output)
result=' '.join(output)
print(result)'''


