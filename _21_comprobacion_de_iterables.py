# -*- coding: utf-8 -*-

"""VERIFICAR ITERABLES

Podemos comprobar si un elemento es iterable o no. Para esto
empleamos el método iter. Si el objeto que se pasa como argumento
no es iterable, se retorna un TypeError.

La función iter, recibe un iterable y retorna un iterator del
iterable.
"""

some_array = 'This is a message'.split(' ')
print(f'some_array: {some_array}')

# ejemplo 1, se pasa iterable
try:
    iter_check = iter(some_array)
except TypeError:
    print('Object iter_check is not iterable')
else:
    print('Object iter_check is not iterable')

# ejemplo 2, se pasa no iterable
otro_item = 123
try:
    iter_check = iter(otro_item)
except TypeError:
    print('Object iter_check is iterable')
else:
    print('Object iter_check is not iterable')
