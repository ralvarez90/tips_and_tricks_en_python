# -*- coding: utf-8 -*-

"""FUNCIÓN FILTER

La función filter recibe una función que se toma como criterio de filtrado, 
cada elemento del iterable que se pasa como segundo argumento es evaluado
con dicha función (que se denomina predicate) y si se retorna True se
agrega al iterador que retorna. 

El iterable a filtrar se puede convertir en una lista, tupla, etc.

La función que recibe filter puede ser el nombre de una función ya
establecido o una expresión lambda.

Nota:
- Recurde que un método de instancia puede invocarse como si fuera un método 
estático, es decir directamente desde la clase siempre y cuando como argumento 
se le pase un objeto de dicha clase. Esta razón es por la que en la línea 33,
podemos pasarle como función str.islower
"""

names: list[str] = 'Juan hugo CANELO Pedro Derek Chad moses linda LUIS'.split(' ')
print(f'names          : {names}')

# ejemplo 1, usando el for
lower_names_v1 = []
for name in names:
    if name.islower():
        lower_names_v1.append(name)
print(f'lower_names_v1 : {lower_names_v1}')

# ejemplo 2, usando filter
lower_names_v2 = list(filter(str.islower, names))
print(f'lower_names_v2 : {lower_names_v2}')

# ejemplo 3, usando filter con expresión lambda
upper_names_v1 = list(filter(lambda name: name.isupper(), names))
print(f'upper_names_v1 : {upper_names_v1}')
