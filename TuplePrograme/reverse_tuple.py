tuples = ('z', 'a', 'd', 'f', 'g', 'e', 'e', 'k')
# Output = ('k', 'e', 'e', 'g', 'f', 'd', 'a', 'z')
t = ()
l = len(tuples)-1
while l >= 0:
    t = t+(tuples[l],)
    l = l-1
print(t)
