a = 10
b = 0
try:  # Getting error here
    c = a/b
    print(c)

except ZeroDivisionError:  # Handling exception here
    print("Division by zero is not allowed")

else:
    print("inside else block")

finally:
    print("inside finally here")

print("Rest of the code")