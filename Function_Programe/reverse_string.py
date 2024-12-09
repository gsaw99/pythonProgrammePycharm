def reverse_string(s):
 output = ''
 i = len(s)-1
 while i>= 0:
    output = output+s[i]
    i = i-1
 print(output)
reverse_string((input("Enter a string here:")))
