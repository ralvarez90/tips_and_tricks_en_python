# -*- coding: utf-8 -*-
import pyfiglet
from random import randint

"""FUENTES CUSTOMIZADAS

Con la librería pygiflet (pythonfigure letter) podemos generar fuentes
custom. La librería tiene el propósito de crear textos bonitos.

La librería se instala con
pip install pyfiglet
"""

# texto a mostrar
title = 'Java    es   mejor   que   Python'

# random font
# fonts = pyfiglet.FigletFont.getFonts()
# font = fonts[randint(0, len(fonts)-1)]

custom_title = pyfiglet.figlet_format(title)
print(custom_title)
print("Aunque esto lo hice en python  :'v")
