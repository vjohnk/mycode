#!/usr/bin/python3
def myFunction(arg1, arg2 , arg3 , *args, **kwargs):
    print('First argument ' + str(arg1))
    print('Second argument ' + str(arg2))
    print('Third argument ' + str(arg3))
    print('Non-keyworded argument ' + str(args))
    print('Keyword argument ' + str(kwargs))

myFunction(1,2,3,4,5,6,7, name='Mandar' , country='India', age=25)
