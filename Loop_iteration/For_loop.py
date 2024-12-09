# For loop:-	This type of loop executes a code block multiple times and abbreviates the code
# that manages the loop variable.
# Nested loops:-	We can iterate a loop inside another loop.
numbers = [4, 2, 6, 7, 3, 5, 8, 10, 6, 1, 9, 2]
squares = []
for value in numbers:
    square = value ** 2
    squares.append(square)
print("The list of squares is", squares)