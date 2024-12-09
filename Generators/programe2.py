def countdown(num):
    print("countdown starting...........")
    while num > 0:
        yield num
        num = num-1

g = countdown(5) # Ye 1-1 karke value dega jab jab app call karo ,ye ek baar ma sab print nahi karega.
                 # Ye memory efficient hai
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


