# -*- coding: utf-8 -*-
import timeit

"""MÓDULO timeit

Si requiere medir el tiempo de ejecución de un código, se 
puede emplear la función timeit.timeit()
"""


def cronometrear(your_code: str) -> str:
    tm = timeit.timeit(your_code, number=1_000)
    return f'Execution time is {tm:.2f} secs.'


if __name__ == '__main__':
    test_code = 'sum(n**2 for n in range(10_000))'
    result_str = cronometrear(test_code)
    print(result_str)
