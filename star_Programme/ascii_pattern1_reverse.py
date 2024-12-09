n = int(input("Enter a number here:"))
for i in range(65, n+65):
    for j in range(i, n+65):
        print(chr(i), end="")
    print()

'''AAAAAA
   BBBBB
   CCCC
   DDD
   EE
   F'''