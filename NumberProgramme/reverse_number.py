# Ye or palindrome number same hai, palindrome ma same number ka opposite bhi same hota hai or
# reverse number kisi bhi number ka ulta kar deta hai.

num = 12345
rev = 0

while num > 0:
    digit = num % 10 # for remainder
    rev = rev * 10 + digit
    num = num//10 # for quotient

#print("Reversed Number: " + str(rev))
print("Reversed Number:", rev)