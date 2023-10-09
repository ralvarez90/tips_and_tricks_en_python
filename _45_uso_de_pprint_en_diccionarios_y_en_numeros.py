# -*- coding: utf-8 -*-
import pprint

"""USO DE PRETTY PRINTER PARA ORDENAMIENTO

Podemos mostrar un diccionario ordenado usando una instancia
pprint.PrettyPrinter y asignandole True al parámetro sort_dicts.

De igual forma si asignamos True al parámetro underscore_numbers
los números impresos con un PrettyPrinter se mostraran con el
caracter underscore como seprador."""

# diccionario
some_dict: dict[str, int] = {
    'c': 2,
    'b': 3,
    'y': 5,
    'x': 10,
}

# lista de entero
pp = pprint.PrettyPrinter(sort_dicts=True, underscore_numbers=True)
pp.pprint(some_dict)
pp.pprint(10**8)
