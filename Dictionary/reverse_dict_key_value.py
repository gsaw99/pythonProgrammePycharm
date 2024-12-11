# Method1
'''d = {"a": 1, "b": 2, "c": 3}
rev = dict((v, k) for k, v in d.items())
print(rev)'''

# Method2
d = {"a": 1, "b": 2, "c": 3}
d1 = {}
for key, value in d.items():
    d1[value] = key
print(d1)

# Method2
'''d = {"a": 1, "b": 2, "c": 3}
d1 = {}
for k, v in d.items():
    d1[v] = d1.get(v, [] +[k])
print(d1)'''
# Method3
'''d = {"a": 1, "b": 2, "c": 3}
rev = dict(map(reversed, d.items()))
print(rev)'''



