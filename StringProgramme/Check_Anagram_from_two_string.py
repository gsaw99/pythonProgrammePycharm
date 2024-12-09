'''Input : s1 = "dad"
        s2 = "bad"
Output : The strings aren't anagrams.'''


str1 = "listen"
str2 = "silent"
if (sorted(str1) == sorted(str2)):
    print("The strings are anagrams.")
else:
    print("The strings aren't anagrams.")
