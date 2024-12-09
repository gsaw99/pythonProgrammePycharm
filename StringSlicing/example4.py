s='code yug'
result=s[-1:-4:-1] #guy
print(result)
result=s[-1:-5:-2] #gy
print(result)
result=s[-2:-6:2] #empty ayega
print(result)
result=s[-1::-1] # guy edoc
print(result)
result=s[-3:-11] # agar step nahi diya hua hai to bydefault +1 samjha jata hai
print(result) # empty ayega because ye forward direction ma jayega to isko kuch bhi nahi milega
result=s[-1:-1:-1] # empty ayega, -1 se start hai or -1 stop bhi hai isliye -1 wala bhi print nahi hoga,
                    # q ki stop value kabhi print nahi hota hai
print(result)
result=s[:-4:-1] #guy , if it is negative slicing then its start from -1 only
print(result)