# -*- coding: utf-8 -*-

"""INTERCAMBIO O SWAPPING

Mediante las tuplas, podemos intercambiar los valores
almacenados en dos variables. Se suelen omitir los
paréntes, ver ejemplo 1.

Operador xor, el operador lógico xor (or exclusivo)
se puede emplear para este mismo propósito. No se
le ve mucho sentido pero se ve mmdor. Requiere
de 3 pasos.
"""


# ejemplo 1,
x, y = 1, 2
print('Antes del intercambio:')
print(f'x={x}, y={y}')

x, y = y, x     # equivalente a (x, y) = (y, x)
print('Después del interacambio:')
print(f'x={x}, y={y}\n')


# ejemplo 2, uso de xor
print('Ejemplo 2, usando xor')
x, y = 1, 2
print('Antes del intercambio:')
print(f'x={x}, y={y}')

x ^= y          # x = x^y
y ^= x          # y = y^x
x ^= y          # x = x^x
print('Antes del intercambio:')
print(f'x={x}, y={y}\n')
