class Factory:
    __a = 10 # ek baar private karne ke baad isko under se hi access kar sakte hain ,outside se nahi.
    b = 20
    def __hello():
       print("hello world")
    __hello()  # ek baar private karne ke baad isko method ke under se hi access kar sakte hain ,outside se nahi.

print(Factory.b)
print(Factory.hello)
print(Factory.a)
