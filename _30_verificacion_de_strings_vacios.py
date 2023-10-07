# -*- coding: utf-8 -*-

"""VERIFICACIÓN DE STRINGS VACIOS

Recordemos que todos los objetos en python pueden evaluarse
como booleanos. Todos los objetos diferentes a None, 0, [], 
(), {}, False, '' se evalúan como verdaderos.

Por lo anterior, la forma más fácil de evaluar si un string es
vacío es usando el operador not."""

msg: str = input('Ingresar string: ')
if not msg:
    print('El string es vacío')
else:
    print(f'Se ingresó "{msg}"')
