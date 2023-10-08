# -*- coding: utf-8 -*-
import os.path
import csv

"""ESCRIBIENDO ARCHIVOS

Empleamos la función open para crear un archivo de texto. Se suele
usar junto la declaración with.

La declaración with se utiliza para simplificar la gestión de recursos,
como archivos, conexiones de red o bases de datos.

El bloque with establece un contexto y garantiza que se ejecute una
porción de código específico antes y después de dicho contexto.

La sintaxis básica es:
with recurso as alias:
    codigo dentro de contexto
codigo fuera del contexto

Podemos usar open para generar un csv, la librería de pandas junto con
algún dataframe o usar el módulo csv.
"""

names = ['Juan Dominguez', 'Hugo Sanchez', 'Pedrito Sola', 'Rodrigo Alvarez']
with open('names.csv', 'w') as file:
    for name in names:
        file.write(name)
        file.write('\n')

# leemos archivo
if os.path.exists('names.csv'):
    with open('names.csv', 'r') as file:
        print(file.read())

# delete file
if os.path.exists('names.csv'):
    os.remove('names.csv')
print('-'*50)

# uso de módulo csv
with open('names.csv', 'w') as file:
    for name in names:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow([name])

# leemos archivo y eliminamos
with open('names.csv', 'r') as file:
    print(file.read())

if os.path.exists('names.csv'):
    os.remove('names.csv')
