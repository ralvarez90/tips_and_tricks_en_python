# -*- coding: utf-8 -*-

"""ACCESO A ÍNDICES

Dada cualquier secuencia, enumerate recordemos que nos retorna una 
colección de tuplas de la forma (n, seq[n]) donde n es un índice del 
iterable y seq[n] el elemento correspondiente a dicho índice.
"""

# ejemplo 1, uso enumerate en un string
string_test = 'string'
for index, value in enumerate(string_test):
    print(f'string_test[{index}] -> {value}')

# ejemplo 2, lista de tuplas
otra_lista = list(enumerate(string_test))
print(otra_lista)
