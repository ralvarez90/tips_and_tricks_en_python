# -*- coding: utf-8 -*-
from functools import reduce

"""APLANAR LISTAS ANIDADAS

Recordemos que una lista anidada es aquella que se encuentra
dentro de otra.

Podemos aplanar listas anidadas usando el método sum. Se
recibe la matriz y una lista vacía como segundo argumento.

Otro mecanismo es empleando la función reduce, reduce del método
functools. Este se emplea para aplicar a una función a una 
secuencia de elementos.
"""

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'matriz    : {matriz}')

# uso de función sum
flatten_v1 = sum(matriz, [])
print(f'flatten_v1 : {flatten_v1}')

# uso de redice
flatten_v2 = reduce(lambda x, y: x+y, matriz)
print(f'flatten_v2 : {flatten_v2}')
