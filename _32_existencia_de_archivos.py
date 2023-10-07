# -*- coding: utf-8 -*-
import os.path

"""EXISTENCIA DE ARCHIVOS

Empleando el módulo os, podemos verificar la existencia de 
archivos. 

Cuando se trabajen con archivos, es importante verificar la
existencia de estos antes de manipularlos. Esto evita
errores en tiempo de ejecución.
"""

filename = 'test_file.txt'

file = os.path.exists(filename)
if file:
    os.remove(filename)
else:
    print(f'The file "{filename}" dont exists')
