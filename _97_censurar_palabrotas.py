# -*- coding: utf-8 -*-
from better_profanity import profanity

"""CENSURADOR DE GROSERIAS

Empleando la librería better_profanity, podemos sensurar con asteriscos
las palabras que se concideren groserias en inglés.

"""

texto = 'I hate this shit'
texto_censurado = profanity.censor(texto)
print(texto_censurado)

if profanity.contains_profanity(texto):
    print('Te vamos a lavar la boca con jabón.')
