num = int(input("Enter a number of rows here:"))
for i in range(1, num+1):
    #for k in range(1,num+1-i):
    for k in range(num-i):
        print("", end=" ")

    for j in range(1, 2*i):
        print("*", end=' ')

    print()

'''   * 
    * * * 
   * * * * * 
  * * * * * * * 
 * * * * * * * * * '''