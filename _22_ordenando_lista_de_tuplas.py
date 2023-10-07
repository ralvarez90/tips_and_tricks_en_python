# -*- coding: utf-8 -*-
from operator import itemgetter
from typing import List, Tuple

"""ORDENANDO LISTA DE TUPLAS

Método itemgetter
Esta función se puede emplear para ordenar listas que contengan
tuplas. Este método se pasa como argumento al key en el método
sorted."""

persons: List[Tuple[str, str]] = [
    ('Juan', 'Domingues'),
    ('Rodrigo', 'Álvarez'),
    ('Vicente', 'Dario'),
    ('Lesly', 'Beltrán'),
]

# ordenamos por apellidos
sorted_by_fnames = sorted(persons, key=itemgetter(0))
sorted_by_lnames = sorted(persons, key=itemgetter(1))
print(f'sorted_by_fnames: {sorted_by_fnames}')
print(f'sorted_by_lnames: {sorted_by_lnames}')
