# -*- coding: utf-8 -*-
import sys

"""TAMAÑO EN MEMORIA

Si queremos saber cuanto almacenamiento en memoria ocupa
un objeto podemos emplear el método sys.getsizeof(obj) que
retorna un entero que represente el tamaño en bytes."""


def getsize(item: object) -> int:
    return sys.getsizeof(item)


# ejemplo 1, algunos objetos
some_int = 1
some_char = 'a'
some_float = 0.0
print(f'sys.getsizeof({some_int}) = {getsize(some_int)} bytes')
print(f'sys.getsizeof({some_char}) = {getsize(some_char)} bytes')
print(f'sys.getsizeof({some_float}) = {getsize(some_float)} bytes')

# ejemplo 2, iterables
some_list = [i for i in range(1, 6)]
some_tupl = tuple([i for i in range(1, 16)])
some_dict = {i: f'item-{i}' for i in range(1, 6)}
print(f'sys.getsizeof({some_list}) = {getsize(some_list)} bytes')
print(f'sys.getsizeof({some_tupl}) = {getsize(some_tupl)} bytes')
print(f'sys.getsizeof({some_dict}) = {getsize(some_dict)} bytes')
