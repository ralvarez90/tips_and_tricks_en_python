# -*- coding: utf-8 -*-
from typing import List

"""ASERCIONES - AFIRMACIONES

Se emplea la sentencia assert con fines de pruebas y 
debuging, permite atrapar excepciones de manera temprana.

Toman dos argumentos, una condición y un mensaje opcional.
La sintaxis es de la forma
assert <condicion>, [error message]

Si no se cumple la aserción, se lanza un AssertionError.
"""

names = ['Jon', 'Elway', 'peter', 'parker', 'PEDRO']

lower_names: List[str] = []
for item in names:
    assert type(item) == str, 'non-string items in the list'
    if item.islower():
        lower_names.append(item)

# results
print(f'lower_names: {lower_names}')
