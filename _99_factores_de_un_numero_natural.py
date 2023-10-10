# -*- coding: utf-8 -*-

"""FACTORES DE UN NATURAL

Los factores de un entero natural n, son todos los números dentro
del rango [1, n] que son divisores de este, es decir, si tenemos un
entero m en el rango, si n%m == 0, entonces m es factor de n.


Notas:
- Todo natural n tiene como factores al 1 y a si mismo."""


def factors_of_v1(n: int) -> list[int]:
    assert n >= 1, 'n cannot be < 1'
    return [m for m in range(1, n+1) if n % m == 0]


def factors_of_v2(n: int) -> list[int]:
    assert n >= 1, 'n cannot be < 1'
    factors = []
    for m in range(1, n+1):
        if n % m == 0:
            factors.append(m)
    return factors


# test
some_integer = int(input('Ingresar entero: '))
print(f'factors_of_v1({some_integer}) = {factors_of_v1(some_integer)}')
print(f'factors_of_v2({some_integer}) = {factors_of_v2(some_integer)}')
