s = "altimetrik"
vowels = ["a", "e", "i", "o", "u"]
count = 0
vowel_word = ''
for i in range(len(s)):
    if s[i] in vowels:
        vowel_word = vowel_word+s[i]
        count = count+1
print(vowel_word, ":", count)