# if step value is positive, move in forward direction
# if step value is negative, move in backward direction
# str[start:stop:step]
s='PYTHON PROGRAMMING'
result=s[::-2]
print(result) # GIMROPNHY
result=s[2:3:-1]
print(result) # empty ayega q ki mismatch ho raha hai, stop value positive hai but
                # step negative hai jo ki backward direction ma jayega
result=s[-15:-16]
print(result) # empty string ayega q ki bydefault step value +1 rahega,
              # jo ki forward direction ma jayega or hamko value nahi milega
result=s[-15:-16:-1]
print(result) # H

result=s[-6:7:-2]
print(result) # AGR

result=s[4:-8] # start from 4 and stop is -8 and bydefault step is +1
print(result) # ON PRO

result=s[9:-10] # step value bydefault is +1
print(result) # empty string

result=s[9:-10:-1]
print(result) # O

result=s[22::-6] # yahan 22 index ka value nahi hai ,isliye ye last positive value ko consider karega
                 # or wahan se start karega , stop value last negative tak jayega and step value -6 ka hai
print(result) # GRN

result=s[2:-22:-1] # ye -22 tak jayega but yahan -22 nahi hai to ye negative ma last tak jo value hai
                  # usko consider karega
print(result) # TYP

result=s[15::-2]
print(result) # IMROPNHY

result=s[-15::-2]
print(result) # HY

result=s[7:-1]
print(result) # PROGRAMMIN





