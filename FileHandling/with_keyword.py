# b= it binary mode


with open('text.txt', 'r') as file:
    data = file.read()
    print(data)

with open('text.txt', 'w') as file:
    data = file.write("I am the boss only") # Ye overwride kar deta hai(pahle wala ko hata deta hai
    print(data)


with open('text.txt', 'a') as file:
    data = file.write("I am the boss only2") # Ye pahle wale line ke badd add ho jata hai
    print(data)