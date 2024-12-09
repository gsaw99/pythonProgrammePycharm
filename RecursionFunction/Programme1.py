import sys
print(sys.getrecursionlimit())  # know the limit of recursion
sys.setrecursionlimit(400)  # set the limit
print(sys.getrecursionlimit())
i = 0
def demo():  # 2nd call from demo()
    global i
    i = i+1
    print("Hello", i)  # 3rd Print Hello
    demo()  # 4th call again n again means ye demo() ,demo function ko call karega


demo()   # 1st call here , Calling from outside function



