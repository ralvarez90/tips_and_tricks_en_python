# -*- coding: utf-8 -*-

"""SEPARADORES EN NÚMEROS

Podemos generar números dentro de strings agregando separadores
que ayuden a su lectura."""
largos: list[int] = [12988667, 8281882831, 992891828381, 12332333239999123]
from_largos_v1: list[str] = ['{:,}'.format(num) for num in largos]
from_largos_v2: list[str] = [f'{num:_}' for num in largos]

print('largos         = {}'.format(largos))
print('from_largos_v1 = {}'.format(from_largos_v1))
print('from_largos_v2 = {}'.format(from_largos_v2))
