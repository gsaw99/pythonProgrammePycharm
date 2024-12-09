# Tuples are an immutable data type, meaning their elements cannot be changed after they are generated.
# Each element in a tuple has a specific order that will never change because tuples are ordered sequences.
# Python program to show how to create a tuple
empty_tuple = () # Creating an empty tuple
print("Empty tuple: ", empty_tuple)
int_tuple = (4, 6, 8, 10, 12, 14) # Creating tuple having integers  
print("Tuple with integers: ", int_tuple)
mixed_tuple = (4, "Python", 9.3) # Creating a tuple having objects of different data types
print("Tuple with different data types: ", mixed_tuple)
nested_tuple = ("Python", {4: 5, 6: 2, 8: 2}, (5, 3, 5, 6)) # Creating a nested tuple
print("A nested tuple: ", nested_tuple)