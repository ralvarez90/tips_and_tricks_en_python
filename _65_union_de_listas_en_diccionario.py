# -*- coding: utf-8 -*-

"""UNIÓN DE 2 LISTAS EN UN DICCIONARIO

Empleando la función zip podemos juntar o comprimir  listas
obteniendo un objeto zip con tuplas. Este objeto zip al ser
iterable puede pasarse como argumento a un dict, list, tuple,
etc.

Usamos la clase dict para obtener un diccionario a parit de un
zip con elementos de dos dimensiones,.
"""

# listas
lista1 = ['name', 'age', 'country']
litsa2 = ['Yoki', 33, 'Angola', 'Luanda']

# diccionario
diccionario = dict(zip(lista1, litsa2))
print(f'diccionario: {diccionario}')
