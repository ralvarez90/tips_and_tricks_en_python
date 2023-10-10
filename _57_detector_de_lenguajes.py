# -*- coding: utf-8 -*-
from langdetect import detect
import langdetect
"""DETECTOR DE LENGUAJES

Empleando el paquete langdetect podemos detectar hasta 55 lenguajes.
"""

message = 'Este es el texto a analizar'
lang = detect(message)
print(f'lang: {lang}')
