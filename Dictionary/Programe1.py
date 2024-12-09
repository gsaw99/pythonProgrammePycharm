myDict = {
    "Name": "Gopal",
    "Roll_no": 123,
    "Class": "Science"
}
dic = myDict.keys() # Only keys ayega
print(dic)
value = myDict.values() # Only values ayega
print(value)
item = myDict.items() # keys and values both ayega
print(item)
key = myDict.get("Name")
print(key)
myDict.update({"address" : "dhanbad"})
print(myDict)