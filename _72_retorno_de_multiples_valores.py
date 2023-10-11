# -*- coding: utf-8 -*-

"""RETORNO DE MÚLTIPLE VALORES

Como bien sabemos python no soporta retorno múltiple, en su lugar
retornamos una tuplas y si se desean se pueden extraer los elementos
de la tupla de forma individual.
"""


def some_values():
    return 1, 2, 3


values = some_values()
a, b, c = some_values()
print(f'values: {values} with type: {type(values)}')
print(f'a, b, c: {a}, {b}, {c} with type: {type(a)}')
