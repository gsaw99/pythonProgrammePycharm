# input:a4k3b2 iska matlab hai a ke badd 4th number pe kaun sa digit ayega
# output:aeknbd
# unicode:a=97, b=98, A=65, B=66
# print(ord(a))-->97 change character to unicode value
# print(chr(97))-->a change unicode value to character
s = 'a4k3b2'
output = ''
for ch in s:
    if ch.isalpha():  # jaise hi degit ayega ye else part ma jayega
        output = output+ch
        x = ch  # x=a
    else:
        d = int(ch)   # yahan ch ko int type casting kar diya taki add ho jaye integer ma
        output = output+chr(ord(x)+d)  # 97+4=chr(101)=e
print(output)

