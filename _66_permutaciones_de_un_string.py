# -*- coding: utf-8 -*-
import itertools

"""PERMUTACIONES DE UN STRING

Recordemos que un string es una secuencia de caracteres. Empleando el módulo 
itertools tenemos una serie de herramientas para crear e iterar a través de 
iterables de manera eficiente. Entre algunos de sus métodos tenemos:

count(start, step)
Genera un iterador infinito que devuelve start, start+step, start + 2*step, ...

cycle(iterable)
Genera iterador ciclico con los elementos del iterable.

repeat(iterable, times)
Genera un iterador que recorre el iterable las veces indicadas por el parámetro times.

chain(itarable1, iterable2, ...)
Genera un iterador que combina los iterables que recibe en 1 solo

islice(iterable, start, stop, step)
Gener aiterador de iterable, con inicio en start, pausa en stop y step.

product(iterable1, iterable2, ...)
Genera iterador del producto cartesiano entre los iterables que recibe
como argumentos.

combinations(iterable, r)
Genera todas las combinaciones de longitud r de elementos del iterble

permutations(iterable, r)
Genera todas las permutaciones de longitud r de elementos del iterable
"""


def get_permutations_v1(s: str):
    arr = []
    for p in itertools.permutations(s):
        arr.append(''.join(p))
    return arr


def get_permutations_v2(s: str):
    return [f'{a}{b}{c}' for a, b, c in itertools.permutations(s)]


# run app
if __name__ == '__main__':
    s = 'ABC'
    print(f'P(s, len(s)) : {get_permutations_v1(s)}')
    print(f'P(s, len(s)) : {get_permutations_v2(s)}')
