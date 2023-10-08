# -*- coding: utf-8 -*-
import timeit
import sys


"""GENERADORES

Se crean de forma silimar a las listas por comprensión, la diferencia 
es que un generador va entregando cada uno de sus elementos de forma
perezosa, es decir, genera sus elementos bajo demanda.

Los generadores generan 1 elemento a la vez, esto los hace más eficientes
tanto en ejecución como en el uso de recursos.

Se emplean los paréntesis para craer generadores por comprensión.
"""


def timer(_, code: str) -> str:
    """Function to check time excecution.
    """
    exc_time = timeit.timeit(code, number=1000)
    return f'{_}: excecution time is {exc_time:.2f}'


def memory_size(_, code) -> str:
    """Function to check memory allocation.
    """
    size = sys.getsizeof(code)
    return f'{_}: allocated memory is {size} bytes'


# entry point
if __name__ == '__main__':
    one = 'Generator'
    two = 'List comprehension'
    print(timer(one, 'sum((num**2 for num in range(100_000)))'))
    print(timer(two, 'sum([num**2 for num in range(100_000)])'))
    print('-'*50)
    print(memory_size(one, sum((num**2 for num in range(100_000)))))
    print(memory_size(two, sum([num**2 for num in range(100_000)])))
