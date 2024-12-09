# The difference between these function, using discard() function if the item does not exist in the set
# then the set remain unchanged whereas remove() method will through an error.

'''set1 = {1, 2, 3, 5, 6, 7}
set1.remove(2)
print(set1)'''

set1 = {"apple", "banana", "cherry"}

set1.remove("banana")

print(set1)