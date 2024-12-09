# Staic Method ko koi matlab nahi hai object instance se, @staticmethod
# class method cls leta hai argument ma, @classmethod

class Student:

    def a(self):  # instance method
        print("Hi Girls Student")
    @classmethod
    def b(cls):  # isko object se koi matlab nahi hai, isko hamlog class ke through or object se bhi call kar
                 # sakte hain, ye argument ma cls leta hai
        print("Hi Boys Student")
    @staticmethod # isko object se koi matlab nahi hai, isko hamlog class ke through or object se bhi call kar
                  # sakte hain, iske bracket ma koi special argument nahi hota hai.
    def c():
        print("By All")
        print("Visit Again in my class in future")
obj = Student()
obj.a()
Student.b()
obj.b()
Student.c()
obj.c()