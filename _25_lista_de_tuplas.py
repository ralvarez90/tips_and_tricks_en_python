# -*- coding: utf-8 -*-

"""LISTAS DE TUPLAS CON ENUMERATE

La función enumerate recibe un iterable y retorna una lista de tuplas donde el
primer elemento de cada tupla es un entero para enumerar."""

dias_semana = ['domingo', 'lunes', 'martes', 'miercoles',
               'jueves', 'viernes', 'sabado']
enum_week = enumerate(dias_semana, start=1)
print(f'enum_week :')
for item_tuple in enum_week:
    print(item_tuple)
