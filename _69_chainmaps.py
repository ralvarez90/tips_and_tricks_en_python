# -*- coding: utf-8 -*-
from collections import ChainMap

"""USO DE CHAINMAPS

Un ChainMap es un tipo de estructura de datos que permite combinar
múltiples directorios en un mismo objeto, creando una especie de
cadena de búsqueda de diccionarios.
"""

# diccionarios
d1 = {'name': 'John', 'sex': 'male'}
d2 = {'name': 'Shasa', 'sex': 'female'}

d1d2_cm = ChainMap(d1, d2)
print(f'd1     : {d1}')
print(f'd2     : {d2}')
print(f'd1d2_cm: {d1d2_cm}')
print(f'd1d2_cm.keys()  : {d1d2_cm.keys()}')
print(f'd1d2_cm.values(): {d1d2_cm.values()}')
