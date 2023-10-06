# -*- coding: utf-8 -*-

"""IMPRIMIR HORIZONTAL

Parámetro end
Empleando el nombre del parámetro end de la función print,
podemos establecer el caracter que se agrega al final de 
cada que se use. Por default el caracter asignado al final
es el salto de línea.

Parámetro sep
Este indica el caracter que se le agregará a cade elemento que
se le pasa como argumento a la función print, ver ejemplo 2.
"""

# ejemplo 1, iteramos lista
algunos_enteros = [i for i in range(1, 6)]
for x in algunos_enteros:
    print(f'{x}', end=' ')
    if x == algunos_enteros[-1]:
        print()

# ejemplo 2, agregamos / como final de cada impresión.
print('mm', 'dd', 'yyyy', sep='/')
print('10', '03', '1990', sep='/')
