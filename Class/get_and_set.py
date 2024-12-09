class Employee:

    def __init__(self, nm, ag):
        self.name = nm
        self.age = ag

e1=Employee("Gopal", 33)
e2=Employee("Mohan", 35)
print(getattr(e1,'age')) # By using this we can get object value
setattr(e2, 'name', 'jay') # By using this we can change attribute value
print(e2.__dict__)
delattr(e2, 'age') # using for delete object
print(e2.__dict__)
print(hasattr(e1, 'name')) # Ye check karta hai ki is attribute ke pass name name ka variable hai ki na