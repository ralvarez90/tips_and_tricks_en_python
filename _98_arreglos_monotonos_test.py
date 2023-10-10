# -*- coding: utf-8 -*-

"""ARREGLOS MONÓTONOS

Se dice que un arreglo es monótono si está ordenado
de forma ascendente o descendente.

Funcion all
Recordemos que la función all se emplea para verificar una
condicion en todos los elementos de un iterable.
"""


def is_monotonic(numbers: list) -> bool:
    if all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1)):
        return True
    elif all(numbers[i] >= numbers[i+1] for i in range(len(numbers)-1)):
        return True
    return False


# algunos arreglos
lista1 = [4, 5, 5, 7]
lista2 = [4, 9, 2, 5]
print(f'is_monotonic({lista1}) = {is_monotonic(lista1)}')
print(f'is_monotonic({lista2}) = {is_monotonic(lista2)}')
