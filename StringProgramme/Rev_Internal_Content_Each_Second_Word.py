#Using while loop
# Write a program to reverse internal content of every second word present in the given string?
# input:one two three four five six
# index: 0,  1,   2,    3,  4,   5
# output:one,owt,three,ruof,five,xis
'''s = 'one two three four five six'
l = s.split() # seperated by comma,['one', 'two', 'three', 'four', 'five', 'six']
print(l)
l1 = []
i = 0  # i indicates index, initialization
while i<len(l):  # condition
    if i%2 == 0:  # no action for even index
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i=i+1    # increment/decrement
output=' '.join(l1)
print(output)'''

# Using For loop
s = 'one two three four five six'
output = []
l = s.split()
print(l)
for i in range(len(l)):
    if i % 2 == 0:
        output.append(l[i])
    else:
        output.append(l[i][::-1])

result = ','.join(output)
print(output)
print(result)