def Stop_Words(text, k):
    d = {}
    s = text.split()
    for i in s:
        if i in d:
            d[i] = d[i]+1
        else:
            d[i] = 1


    res = []
    for i in d:
        if d[i] >= k:
            res.append(i)
    return res


text = input("Enter a string here: ") # a mouse is smaller then a dog but a dog is stronger
k = int(input("Enter a number here:"))
result = Stop_Words(text, k)
print(result)