d = {'Audi':100, 'BMW':1292, 'Jaguar': 210000, 'Hyundai' : 88}
#i='Audi'
i = input("Enter the key here:")
if i in d.keys():
    print("present", 'value', ':', d[i])
else:
    print("no present")