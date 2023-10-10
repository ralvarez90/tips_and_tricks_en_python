# -*- coding: utf-8 -*-

"""DIFERENCIA ENTRE LISTAS

Podemos usar un for, listas por comprensión o hacer conversiones a conjuntos
invocando el método difference.
"""

# listas
a = [9, 3, 6, 7, 8, 4]
b = [9, 3, 7, 5, 2, 1]
print(f'a: {a}')
print(f'b: {b}')

# diferencia, forma 1
difference = []
for n in a:
    if n not in b:
        difference.append(n)
print(f'difference: {difference}')

# diferencia, forma 2
difference = [number for number in a if number not in b]
print(f'difference: {difference}')

# diferencia, forma 3
difference = list(set(a).difference(set(b)))
print(f'difference: {difference}')
