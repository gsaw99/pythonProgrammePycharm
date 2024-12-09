# Write a program to reverse internal content of each word
#input: Gopal Software Solution
#output: lapog ereawtfos noitulos
s = 'Gopal Software Solution'
l = s.split()
print(l)
l1 = []
for word in l:
    l1.append(word[::-1])
print(l1)
output =' '.join(l1)
print(output)