
'''dict1 = {"first": {"a": 1, "b": 2}, "second": {"c": 3, "d": 4}}
print(dict1["second"]["c"])
print(dict1["second"]["d"])'''

dict1 = { 'first': {'name': 'Ali', 'age': '19'},
        'second': {'name': 'Bob', 'age': '25'}}
print(dict1["first"]["name"])
print(dict1.get("first"))