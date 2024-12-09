class Car:
    owner = 'Mahindra' # class variable

    def method(self, name, model1):
        self.name = name   # local variable,
                           # (note- instance variable constructor ke under define hoga hamesha)
        self.model = model1
        return name, model1
    def method2(self):
        pass

obj1 = Car()
obj2 = Car()
obj3 = Car() # we can create multiple object for one class
print(obj1.method("Maruti", "Swift"))
print(obj2.method("Mahindra", "XUV500"))
print(obj3.method("Mahindra1", "XUV700"))
print(obj1.owner)
