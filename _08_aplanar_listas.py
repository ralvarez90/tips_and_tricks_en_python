# -*- coding: utf-8 -*-
import itertools

"""APLANAR LISTAS ANIDADAES

Es común tener que convertir matrices en listas de 1 dimensión.
Se puede hacer un un bucle tradicional o empleando el módulo
itertools.

Del módulo itertools la clase chain nos ofrece un método estático
chain.from_iterable, que recibe un iterable de iterables, y 
retorna un iterable de 1 dimensión aplanando los iterables internos.

Otro tercer mecanismo es empleando listas por comprensión, ver
último ejemplo.
"""

# forma 1, tradicional
una_matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplanado1 = []
for row in una_matriz:
    for item in row:
        aplanado1.append(item)
print(f'Aplanado1: {aplanado1}\n')

# forma 2, usando itertools
aplanado2 = list(itertools.chain.from_iterable(una_matriz))
print(f'Aplanado2: {aplanado2}\n')

# forma 3, usando list comprehensions
aplanado3 = [item for row in una_matriz for item in row]
print(f'Aplanado3: {aplanado3}\n')
