# and:-	The condition will also be true if the expression is true. If the two expressions a and b are the same,
# then a and b must both be true.
# or:-	The condition will be true if one of the phrases is true. If a and b are the two expressions,
# then an or b must be true if and is true and b is false.
# not:-	If an expression a is true, then not (a) will be false and vice versa.

a = 5          # initialize the value of a
print('Is this statement true?:', a > 3 and a < 5)
print('Any one statement is true?:',a > 3 or a < 5)
print('Each statement is true then return False and vice-versa:', (not(a > 3 and a < 5)))