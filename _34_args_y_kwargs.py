# -*- coding: utf-8 -*-
from numbers import Number
from typing import Any

"""USO DE *args Y **kwargs

1. *args
Recordemos que las funciones y métodos pueden recibir una cantidad 
variable de argimentos, estos se alamcenan dentro de una tupla.

Se emplea *nombre_tupla al definir la función indicando que los
parámetros variables se almacenarán en dicha tupla. Por convensión
se emplea *args como nombre de dicha tupla.

2. **kwargs
Podemos pasarse parámetros nombrados a una función donde cada elemento
se almacenará en un diccionario. Por convensión dicho diccionario
se nombre kwargs. Los keys se almacenan en strings.
"""


def average(*args: Number) -> float:
    return sum(args)/len(args)


def suma_enteros(*numbers: int) -> int:
    total = 0
    for n in numbers:
        total += n
    return total


def show_parameters(**kwargs):
    print('Elementos del diccionario: ')
    for k, v in kwargs.items():
        print(f'kwargs[{k}] = {v}')
    print(f'kwargs : {kwargs}')


# test programa
if __name__ == '__main__':
    print('Ejemplo de *args')
    print(f'some average : {average(1, 0, 3, 4, 5, 5.5, 6):.2f}')
    print(f'1+2+3+4+5    : {suma_enteros(1, 2, 3, 4, 5)}', end='\n\n')

    print('Ejemplo de **kwars')
    show_parameters(name='Rorro', age=33, is_single=False)
