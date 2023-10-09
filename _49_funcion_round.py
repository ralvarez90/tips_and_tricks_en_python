# -*- coding: utf-8 -*-
import math

"""FUNCIÓN DE REDONDEO ROUND

Se emplea para redondear el valor de un número.

Si no recibe un segundo argumento denominado ndigits, retorna
el entero redondeado.

Como alternativas tenemos las funciones math.ceil y math.floor
para poder obtener el techo y el piso de un número. Estas funciones
retornan un entero.
"""

# some numbers
some_numbers = [12.92312, 1, 123.123, 0.000001232, 1.4999, 1.5, 1.99999]

# uso de round(n) y round(n, ndigits=)
print('USO DE FUNCIÓN: round')
for n in some_numbers:
    print(f'n = {n:>9}', end=', ')
    print(f'round(n) = {round(n):>3}', end=', ')
    print(f'round(n, ndigits=2) = {round(n, ndigits=2):>6}')
print('-'*50)

# uso de math.floor y math.ceil
print('USO DE FUNCIONES: math.floor y math.ceil')
for n in some_numbers:
    print(f'n = {n:>9}', end=', ')
    print(f'math.floor(n) = {math.floor(n):>3}', end=', ')
    print(f'math.ceil(n) = {math.ceil(n):>3}')
print('-'*50)
