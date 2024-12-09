# Write a program to sort characters of the string, first alphabet symbols followed by digits.
#input: B4A1D3
#output: ABD134
#s = input("Enter the alphanumeric here: " )
s = 'B4A1D3'
alphabets = []
digits = []
for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)
output = ''.join(sorted(alphabets)+sorted(digits))
print(output)