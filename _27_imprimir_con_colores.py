# -*- coding: utf-8 -*-
import inspect

"""IMPRIMIR CON COLORES

Utilizando códigos de escape ANSI podemos dar formato de salida. Puede verificar
más información en:
https://es.wikipedia.org/wiki/C%C3%B3digo_escape_ANSI

Estos códigos permiten cambiar el color del texto, la posición del cursor y 
otros aspectos de la presentación del texto en una terminal. En Python, puedes 
utilizar estos códigos ANSI para controlar la apariencia del texto en la salida 
estándar.
"""


class Color:
    BLACK = '\033[30m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    RED = '\033[31m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    YELLOW = '\033[33m'


for color_name in inspect.getmembers(Color()):
    if color_name[0].isupper():
        print(f'{color_name[1]}Saludos en color {color_name[0].title()}')
