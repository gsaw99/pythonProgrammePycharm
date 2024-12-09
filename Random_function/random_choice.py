# The random.choice() function selects an item from a non-empty series at random.
# In the given below program, we have defined a string, list and a set. And using the above choice() method,
# random element is selected.
# To select a random element
import random
random_s = random.choice('Random Module') # a string
print(random_s)
random_l = random.choice([23, 54, 765, 23, 45, 45]) # a list
print(random_l)
random_s = random.choice((12, 64, 23, 54, 34)) # a set
print(random_s)
