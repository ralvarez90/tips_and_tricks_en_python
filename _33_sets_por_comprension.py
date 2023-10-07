# -*- coding: utf-8 -*-
from random import randint

"""CONJUNTOS POR COMPRENSIÓN

Se conforma al igual que la listas por comprensión de una
expresión, un rango o secuencia y condiciones si es el caso."""

# ejemplo 1, set de strings
some_words: list[str] = 'LOVE HATE WAR PEACE PEACE WAR'.split(' ')
print(f'some_words: list[str] = {some_words}')
set_words = {word.lower() for word in some_words}
print(f'set_words : set[str]  = {set_words}')

# ejemplo 2, set de enteros
aleatorios: list[int] = [randint(1, 1000) for _ in range(1000)]
filtrados_pares: set[int] = {n for n in aleatorios if n % 2 == 0}
print(f'filrados_pares: set[int]   = {filtrados_pares}')
print(f'donde len(filtrados_pares) = {len(filtrados_pares)}')
