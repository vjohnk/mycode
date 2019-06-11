#!/usr/bin/python3
ans=(lambda z:z*4)
print(ans(5))

items = [2,3,4,5]
squared = list(map(lambda x: x**2, items))
cubed = list(map(lambda x: x**3 , items))
print(squared,cubed)

number_list = range(-5 ,5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

from functools import reduce
product = reduce((lambda x,y: x*y), [1,2,3,4])
print(product)
