class GrandFather:
    def place(self):
        print("This is a GrandFather place")

class Father(GrandFather):
    def room(self):
        print("This is Father room")

class Child(Father):
    pass

obj = Child()
obj.place()
obj.room()  # isme child GrandFather and father dono ka properties le sakta hai
