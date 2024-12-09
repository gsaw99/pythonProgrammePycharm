d1 = {'Audi': 100, 'BMW': 1292, 'Jaguar': 210000, 'Hyundai': 88}
d2 = {'Maruti': 102, 'yamah': 1200, 'sujuki': 2105001, 'Honda': 880}
d1.update(d2) # ye d1 ma update hoga, isliye d1 ko print kiya
print(d1)

# Method2 ,using merge(|) operator
'''d1 = {'Audi':100, 'BMW':1292, 'Jaguar': 210000, 'Hyundai' : 88}
d2 = {'Maruti':102, 'yamah':1200, 'sujuki': 2105001, 'Honda' : 880}
d3=d1|d2
print(d3)'''

#Method3 ,Unpacking Operator (**) is used
'''d1 = {'Audi':100, 'BMW':1292, 'Jaguar': 210000, 'Hyundai' : 88}
d2 = {'Maruti':102, 'yamah':1200, 'sujuki': 2105001, 'Honda' : 880}
result = {**d1, **d2}
print(result)'''