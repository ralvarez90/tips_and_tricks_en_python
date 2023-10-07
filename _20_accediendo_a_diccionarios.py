# -*- coding: utf-8 -*-

"""ACCEDIENDO A DICCIONARIOS

El método keys() de un diccionario nos retorna un iterable
con las claves de un diccionario.

Recordemos que sorted recibe un interable y el iterable de keys
que retorna.

Notas:
- Recordar que a partir de Python 3.7, lo diccionarios son
elementos ordenados.
"""

dict1 = {'name': 'Juan', 'age': 33, 'student': True, 'country': 'mx'}

# acceso a keys, forma 1
llaves1: set = {key for key in dict1.keys()}
print(f'llaves1: {llaves1}')

# forma 2, obtenemos keys
llaves2: set = set(dict1)
print(f'llaves2: {llaves2}')

# ordenamos diccionario
list_from_dict = sorted(dict1)
print(f'dict1: {dict1}')
print(f'list_from_dict: {list_from_dict}')
