'''def even(start, n):
    my_list=[]
    start = 5
    for i in range(start, n):
        if i%2==0:
            my_list.append(i)
            start=start+1

    return my_list
n = int(input("Enter a number here:"))
result = even(5, n)
print(result)'''

def even(start, n):
    my_list=[]
    #start = 5
    for i in range(start, n):
        if i%2==0:
            my_list.append(i)
            start=start+1

    return my_list
n = int(input("Enter a number here:"))
start= int(input("Enter a number here:"))
result = even(start, n)
print(result)