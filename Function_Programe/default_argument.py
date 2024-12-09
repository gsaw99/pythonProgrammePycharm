def hello(a, b, c, d=50): # d is a default parameters, a,b,c is normal parameters
    print(a+b+c+d)

hello(20, 30, 40, 100) # Agar maine yahan d ka value daal diya to ye upar wala default parameters(d) ke value ko override kar dega.
hello(20, 30, 40)# default arguments

