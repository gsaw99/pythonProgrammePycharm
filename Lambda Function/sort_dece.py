city = ['Jaipur', 'Goa',  'Kota', 'Dhanbad', 'Mumbai', 'Delhi' ]
sort = sorted(city, key=lambda x: len(x), reverse=True)
print("sorted words by length:", sort)
