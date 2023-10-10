# -*- coding: utf-8 -*-

"""EXISTENCIA DE SUBSTRINGS EN STRINGS

Podemos emplear el operador in y su negación not in para verificar
la existencia de una subcadena.

Si desea obtener el índice de una subcadeba dentro de otra, usar el
método find. Regresa -1 si no encuentra incidencia.
"""

s = 'Pleas find something you like'

# uso de in
if 'like' in s:
    print(f'"like" is a substring of "{s}"')
else:
    print(f'"like" is not a substring of "{s}"')

# uso de not in
if 'like' not in s:
    print(f'"like" is not a substring of "{s}"')
else:
    print(f'"like" is a substring of "{s}"')

# uso de find
print(s.find('like'))
