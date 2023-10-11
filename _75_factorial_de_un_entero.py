# -*- coding: utf-8 -*-

"""FACTORIAL DE UN ENTERO

Recordemos que dado un entero n>1 el factorial
de n se define como n*n-1*...*2*1"""


def factorial_v1(n: int) -> int:
    assert n >= 1, 'n value cannot be < 1'
    f = 1
    for k in range(2, n+1):
        f *= k
    return f


def factorial_v2(n: int) -> int:
    assert n >= 1, 'n value cannot be < 1'
    return 1 if n == 1 else n*factorial_v2(n-1)


for n in range(1, 30):
    print(f'{n}! -> {factorial_v1(n)}')
    print(f'{n}! -> {factorial_v2(n)}')
