# Method1
num = [10, 0, -1, 7, 8, 10, -67]
'''rev=num[::-1]
print(rev)'''
'''num.reverse()
print(num)
# Method2'''
# Method2
start = 0
end = len(num)-1
while end > start:
    num[start], num[end] = num[end], num[start]
    start = start+1
    end = end-1
print(num)

# Method3

'''def reverse_list(num):
    for i in range(len(num)-1, -1, -1):
        yield num[i]
print(list(reverse_list([10, 0, -1, 7, 8, 10, -67])))'''
