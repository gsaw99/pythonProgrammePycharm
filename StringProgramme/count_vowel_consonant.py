# Method1
#str1="gopalkumarsaw"
'''str1 = input("Enter a string here:")
vowel = 0
consonant = 0
for i in range(0, len(str1)):
    if str1[i] != "": # ye space ke liye hai jo letter ke bitch ma rahta hai like gopal kumar saw
       if str1[i] == "a" or str1[i] == "e" or str1[i] == "i" or str1[i] == "o" or str1[i] == "u" \
          or str1[i] == "A" or str1[i] == "E" or str1[i] == "I" or str1[i] == "O" or str1[i] == "U":
           vowel = vowel+1
       else:
           consonant = consonant+1
print("Total vowel is =:", vowel )
print("Total consonant is =:", consonant)'''

# Method2
str1 = "gopalkumarsaw"
vowels = "aeiou"
count = 0
for i in str1:
    if i.lower() in vowels:
        count = count+1

print("Number of vowels is:", count)

# Method3
