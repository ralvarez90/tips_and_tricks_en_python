# -*- coding: utf-8 -*-
import re

"""MULTIPLES ENTRADAS

Podemos obtener múltiples elementos usando una sola sentencia
input. El truco es usar una expresión regular con su método 
split.

El siguiente ejemplo ingresa una cadena con 3 números separados
por comas y 0 o más espacios.

Ejemplo:
123,    132, 4

re.split retorna una lista con cada uno de los números, map convierte
a entero cada uno de los elementos de la lista y empleando
unpacking se almacenan los valores enteros en las 3 variables a, b y c.
"""

# detecta una coma seguido de 0, 1 o más espacios
pattern = r',\s*'
a, b, c = map(int, re.split(pattern, input('Input 3 numbers: ')))
print(f'Average ({a}+{b}+{c})/3: {(a+b+c)/3}')
