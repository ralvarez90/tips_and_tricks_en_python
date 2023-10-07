# -*- coding: utf-8 -*-
from collections import Counter

"""COUNTING ITEM OCURRENCES

Si desea saber el número de veces que un determinado elemento
aparece o se encuentra dentro de un iterable, se puede emplear la
clase Counter que retorna un diccionario de cuantos elementos 
aparecen en en un iterable.

Cada key del diccionario resultante es un elemento del
iterable.

Las instancias Counter soportan comparación por medio del
operador ==.

Notas:
- Los objetos Counter extienden de dict, y tienen un método
llamado most_common que permiten obteneruna lista con los
n elementos más comunes.
"""

# ejemplo 1, lista de strings
lista1 = ['Juan', 'Hugo', 'Paco', 'Luis', 'Paco', 'Ramiro']
contador = Counter(lista1)
print(f'Conteo en lista1:\n{contador}')
print(f'"Paco" aparece en la lista {contador.get("Paco")} veces\n')

# ejemplo 2, string
some_text = 'Esto es un menesaje.'
print(f'some_text: "{some_text}"')
letter_counter = Counter(some_text.lower())
print(f'Conteo en some_text:\n{letter_counter}')
print(f'3 letras más comunes: {letter_counter.most_common(3)}')
