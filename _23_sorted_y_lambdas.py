# -*- coding: utf-8 -*-

"""ORDENAR LISTAS CON SORTED Y EXPRESIONES LAMBDA

La función sorted es una HOF ya que toma otra función como parámetro.
Podemos asignar una expresión lamdba (que son funciones) al parámetro
key.
"""

# ordenamiento con sorted y lambdas
lista1 = ['mary', 'petter', 'kelly', 'thomas']


# se emplea para usarse como key en sorted
last_char = lambda some_list: some_list[-1]

ordenada1 = sorted(lista1, key=last_char)
print(f'ordenada1: {ordenada1}')

ordenada2 = sorted(lista1, key=len, reverse=True)
print(f'ordenada2: {ordenada2}')
