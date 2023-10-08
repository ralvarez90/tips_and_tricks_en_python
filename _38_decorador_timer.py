# -*- coding: utf-8 -*-
import time
from typing import Callable


"""DECORADOR TIMER

Antes de explicar qué es un decorador, tomemos en cuneta los siguientes
conceptos.

1. Funciones internas
Una función interna es aquella que se implementa dentro de otra.

2. Una función se dice que es ciudado de primera clase, es decir, se
comportan como variables en el sentido de que pueden ser asignadas a 
nombres de variables, ser argumentos de una función, o retornarnse
dentro de una función.

3. Una función de orden superior (HOF) es cualquier función que cumpla
al menos uno de los siguientes criterios.
- Recibe al menos una función como parámetro.
- Retorna otra función.

4. Decoradores
Es una HOF, que recibe una función como argumento y retorna otra.
La función retornada, ejecuta en su interior la función que ses
decorada.

Decorar una función significa agregarle o proveerle funcionalidad
extra.
"""


def timer(func: Callable):
    """Recibe una función, implementa una función interna que ejecuta
    la función como parámetro y al final la retorna.

    Args:
        func (Callable): función que se decora.
    """

    def inner():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        print(f'Run time is {end-start:.2f} secs')

    return inner


@timer
def range_tracker():
    lst = []
    for i in range(100_000_000):
        lst.append(i**2)


# invocamos función
if __name__ == '__main__':
    range_tracker()
