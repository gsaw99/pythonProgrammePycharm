marks = int(input("Enter the marks? "))
if marks > 85 and marks <= 100: # Here, we are checking the condition. If the condition is true, we will enter the block

   print("Congrats ! you scored grade A ...")
elif marks > 60 and marks <= 85: # Here, we are checking the condition. If the condition is true, we will enter the block

   print("You scored grade B + ...")
elif marks > 40 and marks <= 60:  # Here, we are checking the condition. If the condition is true, we will enter the block

   print("You scored grade B ...")
elif (marks > 30 and marks <= 40): # Here, we are checking the condition. If the condition is true, we will enter the block     

   print("You scored grade C ...")
else:
   print("Sorry you are fail ?")