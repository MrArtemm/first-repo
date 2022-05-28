def checker(x):
    if type(x) != int:
        raise TypeError('Please, we need INT')
a = 'dog'
try:
    checker(a)
except TypeError:
    print('ERROR')
