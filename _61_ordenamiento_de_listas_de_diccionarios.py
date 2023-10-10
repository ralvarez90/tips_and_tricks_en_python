# -*- coding: utf-8 --
from operator import itemgetter

"""ORDENAR LISTAS DE DICCIONARIOS

Empleamos el método sorted nuevamente y la función del módulo
operator itemgetter, que se emplea en el key de sorted.
"""

dicts = [
    {'school': 'yale', 'city': 'beijing'},
    {'school': 'cat', 'city': 'cairo'},
]

# ordenamiento por 'school'
sorted_by_school = sorted(dicts, key=itemgetter('school'))
sorted_by_city = sorted(dicts, key=itemgetter('city'))

# resultados
print(f'original        : {dicts}')
print(f'sorted_by_school: {sorted_by_school}')
print(f'sorted_by_city  : {sorted_by_city}')
