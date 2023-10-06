# -*- coding: utf-8 -*-
import calendar

"""CALENDARIOS

El módulo buil-in llamado calendar nos permite realizar muchas
cositas.

calendar.month(year: int, month: int)
Recibe un año y un mes en enteros y retorna un string con el 
calendario de dicho mes.

calendar.isleap(year: int)
Verifica si el año es bisiesto. Retorna un booleano.
"""

# ejemplo 1, calendar.month
mi_mes = calendar.month(1990, 3)
print('calendar.month(1990, 3) : ')
print(mi_mes)

# ejemplo 2, año bisieso
mi_anio = int(input('Año de nacimiento: '))
print(
    f'El año {mi_anio} fue bisiesto: {"Si" if calendar.isleap(mi_anio) else "No"}')
