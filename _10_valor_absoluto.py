# -*- coding: utf-8-*-

"""VALOR ABSOLUTO

Tenemos la función abs que retorna el valor absoluto o un objeto
que soporte de alguna forma la definción de valor absoluto.

Otra forma es emplear la función mapeo iterable. Recibe una función y
un iterable a los cuales va a aplicar la función."""

# ejemplo 1, lista de enteros
some_nums = [-12, 45, -67, -89, -34, 67, -13]
print(f'some_nums: {some_nums}')

# usando listas por comprensión y función abs
abs_values1 = [abs(x) for x in some_nums]
print(f'Absolute values: {abs_values1}')

# usando map
abs_values2 = list(map(abs, some_nums))
print(f'Absolute values: {abs_values2}')
