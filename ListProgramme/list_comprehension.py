'''fruits = ["apple", "banana", "cherry", "kiwi", "mango"] # iterable item
newlist = []

for fruit in fruits:
  if "a" in fruit:
    newlist.append(fruit)

print(newlist)'''

# Provides a shorter syntax while creating a new list from the existing list.
# With list comprehension we can do all that with only one line of code

# syntax:- [expression for item in iterable if condition == True]
# expression ke place ma operation kar sakte hain like fruite*fruite
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]  # iterable item

new_list = [fruit for fruit in fruits if "a" in fruit]  # fruit variable store the value

print(new_list)