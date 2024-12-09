str = "welcome to Miraffa Technologies"
# 0/p:emoclew ot affariM seigolonhceT
word = []
list1 = str.split()       # ['welcome', 'to', 'Miraffa', 'Technologies']
print(list1)
for w in list1:
    word.append(w[::-1])  # ['emoclew', 'ot', 'affariM', 'seigolonhceT']
print(word)
result = ' '.join(word)
print(result)             # emoclew ot affariM seigolonhceT
