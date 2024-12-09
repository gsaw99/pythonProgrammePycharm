'''file = open('text.txt', 'r') # r is indicating read i.e By default(ham de bhi sakte hain or nahi bhi)
data = file.read(5) # if you want to print 5 characters then we need to put number in bracket otherwise print all.
print(data)
file.close()'''

# For Readline(line by line)
'''file = open('text.txt', 'r')
data1 = file.readline()
data2 = file.readline()
data3 = file.readline()
data4 = file.readline()
data5 = file.readline()
data6 = file.readline()
print(data1)
print(data2)
print(data3)
print(data4)
print(data5)
print(data6)  # ek baar data finish ho gaya to phir empty ayega output ma
file.close()'''
# Using for loop for readline
file = open('text.txt', 'r')
data = file.readline()
while data != '':
    print(data)
    data = file.readline()

file.close()
