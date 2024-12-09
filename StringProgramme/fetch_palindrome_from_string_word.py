input = "mamadsfajsdmalayalamasdfsafmadam"

#output = ['mam', 'ama', 'malayalam', 'ala', 'alayala', 'layal', 'aya', 'ala', 'ama', 'madam', 'ada']
result = list(input)
print(result)
output=[]
for i in result:
        output.append(i+i+i)
print(output)
palindrome1='mam,'.join(output)
print(palindrome1)
