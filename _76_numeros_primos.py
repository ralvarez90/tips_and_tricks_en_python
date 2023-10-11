# -*- coding: utf-8 -*-
from numba import njit

"""NÚMEROS PRIMOS

Un número primo es aquel que únicamente es divisible por si mismo y por
la unidad. Generamos una lista con los primeros n primos de la forma
siguiente.

Separando responsabilidades, podemos agregar compilación jit a la
función is_prime y esta emplearla como condición al generar la lista
por comprensión.

Se emplea la librería numba y el decorador @njit.
"""


def prime_numbers_v1(limit: int) -> list:
    primes = []
    for i in range(2, limit):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


@njit
def is_prime(n: int) -> bool:
    # si i=25, i esta en [2, 12]
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


def prime_numbers_v2(limit: int) -> list:
    return [n for n in range(2, limit+1) if is_prime(n)]


print(f'prime_numbers_v1(10) : {prime_numbers_v1(1000)}')
print(f'prime_numbers_v2(10) : {prime_numbers_v2(1000)}')
