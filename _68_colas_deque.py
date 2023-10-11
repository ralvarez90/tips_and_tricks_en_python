# -*- coding: utf-8 -*-
from collections import deque

"""COLAS

Recordemos que una cola es una estructura de datos de tipo
FIFO (First Input First Output), python nos proporciona la
estructura de datos dequeu (cola de dos extremos) que nos
permite trabajar de manera eficiente con colas pero con 
la flexibilidad de operar como pilas.

Algunos de los métodos más comunes de este tipo de colas son:

append, appendleft
Permite agregar elementos de forma default (al final de la cola)
o al 'inicio'.

extend, extendleft
Similar a append pero acá se agregan todos los elementos del iterable
que recibe como argumento.

insert
Permite agrega elementos a la cola en una determinada posición.

pop, popleft
Permite eliminar y extraer el último elemento el primer elemento.
Si se pretende eliminar un elemento de un deque vacío se lanza una
excepción.
"""

# ejemplo 1, append
cola1 = deque([1, 2, 3])
cola1.appendleft(0)
cola1.append(4)
print(f'cola1: {cola1}')

# ejemplo 2, extend
cola1.extend([5, 6])
print(f'cola1: {cola1}')

print('Uso de rotate:')
for i in range(5):
    cola1.rotate()
    print(cola1)

while len(cola1) > 0:
    print(f'Eliminando: {cola1.pop()}, restan {cola1}')
