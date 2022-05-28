def checker(x):
    if type(x) != int:
        raise TypeError('Please, we need INT')
a = 'cat'
try:
    checker(a)
except TypeError:
    print('ERROR')