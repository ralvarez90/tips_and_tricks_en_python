# -*- coding: utf-8 -*-

"""INDICES EN LISTAS DE NÚMEROS

Empleando las funciones enumerate, min y max podemos encontrar
índices de elementos máximo y mínumos de una lista de números."""

# ejemplo 1, uso de enumerate y max
numbers = [12, 45, 67, 89, 34, 67, 13]
print(f'algunos_numeros: {numbers}')

# almacenan tuplas (indice, numero)
max_num_tuple = max(enumerate(numbers, start=0), key=lambda _lst: _lst[1])
min_num_tuple = min(enumerate(numbers, 0), key=lambda _lst: _lst[1])

# resultados
print(f'max_num index : {max_num_tuple[0]}')
print(f'min_num index : {min_num_tuple[0]}')
