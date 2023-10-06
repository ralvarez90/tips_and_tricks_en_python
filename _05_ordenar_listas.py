# -*- coding: utf-8 -*-
import random

"""ORDENAMIENTO DE LISTAS

Las listas tienen un método disponible denominado sort, que
cambia el estado de la lista ordenando sus elementos.

El método sort puede recibir un parámetro reversed booleano
para indicar si se ordena de forma inversa.

Si se recibe una función en el parámero key, dicho método
se utilizará como criterio de ordenamiento. Ese key method
se aplica a cada uno de los elementos de la lista y devuelve
el valor que se utiliza como criterio de ordenamiento.
"""


# ejemplo 1, lista de 10 enteros aleatorios entreo 1 y 100
numeros = [random.randint(1, 100) for _ in range(10)]
print(f'Lista generada: {numeros}')
numeros.sort()
print(f'Lista ordenada (normal) : {numeros}')
numeros.sort(reverse=True)
print(f'Lista ordenada (reverse): {numeros}')

# ejemplo 2, lista de strings
nombres = ['hugo', 'paco', 'luis', 'tomas', 'clarita']
nombres.sort()
print(f'nombres.sort()                      :  {nombres}')
nombres.sort(reverse=True)
print(f'nombres.sort(reverse=True)          :  {nombres}')
nombres.sort(key=len)
print(f'nombres.sort(key=len)               :  {nombres}')
nombres.sort(key=len, reverse=True)
print(f'nombres.sort(key=len, reverse=True) :  {nombres}')
