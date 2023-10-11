# -*- coding: utf-8 -*-

"""UNPACKING DE LISTAS

El operador * se conoce como 'unpacking' operator, y se emplea para
poder desempacar de elementos de una lista y asignar.
"""


def get_first_item(lst: list):
    assert len(lst) > 0, 'len(lst) cannot be <= 0'
    first, *_ = lst
    return first


# ejemplo 1,
names = 'Jonh Mary Lisa Mary'.split(' ')
boy_name,  *girls_names = names
print(f'boy_name    : {boy_name}')
print(f'girls_names : {girls_names}')

# ejemplo 2,
print(get_first_item(names))
