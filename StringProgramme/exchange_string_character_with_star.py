str1 = "selenium"
# output= "s*l**nium, first e ma 1 star ayega, second e ma two star ayega
count = 0
for i in str1:
    if i == "e":
        count = count+1
        print("*",  end="")
    else:
        print(i, end="")
