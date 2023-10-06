# -*- coding: utf-8 -*-

"""UNIR DICCIONARIOS

Dados dos diccionarios, sea d1 y d2, si queremos obtener un diccionario d3 resultado
de unir d1 y d2, podemos usar el operdor | y el operador **

Operador |
Este operador une los dos diccionarios, en donde si un key está repetido, se le asigna
el valor del diccionario más a la derecha

Operador **
Recordemos que ** es el operador de destructuración, que nos permite hacer el trucazo
de magazo del ejemplo 2.
"""

# ejemplo 1, opeardor merge
d1 = {'ramon': 12, 'raulsito': 22}
d2 = {'hugo': 34, 'paco': 25, 'luis': 46, 'ramon': 0}
d3 = d1 | d2
print(f'd1  |  d2    <-> {d3}')

# ejemplo 2, destructuración con **
d3 = {**d1, **d2}
print('{**d1, **d2} <-> %s' % (d3))
