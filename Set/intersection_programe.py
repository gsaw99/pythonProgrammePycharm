# Using intersection() method

'''set1 = {1, 2, 10, 5, 6, 7}
set2 = {0, 5, 3, 9, 0, 4}
matched_value = set1.intersection(set2)
print(matched_value)'''  # Dono ma jo match hoga wo value print hoga

# we can perform the intersection of more than two sets at a time,
'''set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5} 
common_elements = set1.intersection(set2, set3)  # Find the common elements between the three sets 
print(common_elements)'''  # Print the common elements

# Using & operator
Days1 = {"Monday","Tuesday", "Wednesday", "Thursday"}
Days2 = {"Monday","Tuesday","Sunday", "Friday"}
print(Days1&Days2) #prints the intersection of the two sets