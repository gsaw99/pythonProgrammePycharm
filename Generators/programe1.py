#Generator is a function which is responsible to generate a sequence of values by using yield keyword to
# return values.
# isme all value store nahi hota hai, ye 1-1 kar ke leta hai value ko or 1-1 karke return karta hai.

def my_gen():
    yield "hello world"
    yield "i am gopal"
    yield "tester"

g = my_gen()  # jab function call hoga to my_gen() ka statement return nahi hoga q ki ye Yield keyword hai
              # jo ki generator hai, yahan uska object return hoga.
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))
for i in g:
    print(i)




