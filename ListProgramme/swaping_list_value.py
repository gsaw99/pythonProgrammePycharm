my_list = [1, 2, 3, 4, 5]
#  output=[5, 2, 3, 4, 1]
my_list[0], my_list[4] = my_list[4], my_list[0]
print(my_list)