# Method1
s = "altimetrik"
vowels = "aeiou"
count = {}.fromkeys(vowels, 0)  # returns the specified key and value, dict.foromkeys(keys, value)
for i in s:
    if i.lower() in vowels:
        count[i] = count[i]+1
print(count)


# Nethod2
'''s = "altimetrik"
vowels = "aeiou"
vowel_word = {}.fromkeys(vowels, 0)
for i in s:
    if i.lower() in vowels:
        vowel_word[i] = vowel_word[i] + 1
        # count=count+1
for vowel in vowel_word:
    print(vowel, ":", vowel_word[vowel])'''
