# The random.randrange() function selects an item randomly from the given range defined by the start,
# the stop, and the step parameters. By default, the start is set to 0. Likewise, the step is set to 1 by default.
# To generate value between a specific range
import random
num = random.randrange(1, 10)
print(num)
num = random.randrange(1, 10, 2)
print(num)
