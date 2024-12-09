tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Objects")
try:
    del tuple_[3]    # Deleting a particular element of the tuple
    print(tuple_)   # 'tuple' object does not support item deletion
except Exception as e:
    print(e)
# Deleting the variable from the global space of the program
del tuple_    # Trying accessing the tuple after deleting it
try:
    print(tuple_)
except Exception as e:
    print(e)