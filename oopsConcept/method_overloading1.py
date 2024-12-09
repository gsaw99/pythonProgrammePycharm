class Name:

    def find_name(self, firtstname="", lastname=""):
        print("welcome", firtstname, lastname)

obj1 = Name()
obj1.find_name()
obj1.find_name("Gopal")
obj1.find_name("Gopal", "Kumar")