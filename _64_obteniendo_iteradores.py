# -*- coding: utf-8 -*-

"""MÉTODO __iter__

Antes explicaremos algunos conceptos.

1. Un iterable es un objeto que implemente el método __iter__ o
el método __getitem__ de forma que pueda tomar índices consecutivos
empezando desde 0 lanzando una excepción IndexError  ante índices 
inválidos. Estos siempre pueden ser pasados al método build-int
iter para que retorne un iterador a partir del mismo.

2. Un iterador es un objeto que además del método __iter__ implementa
el método __next__, el cual al se llamado retorna el siguiente item del
mismo o la excepción StopIteration si el iterador ha sido consumido.

3. Un ciclo for in siempre empieza llamando __iter__ del cual obtiene
un iterador a partir del iterable de turno.


En python para que un objeto sea un iterador debe cumplir con el
llamado Protocolo Iterador.

Para crear un iterador de un objeto se emplea la función iter, una vez
que el iterador es creado los elementos uno a la vez utilizando el 
método next().
"""


class MiIterable:

    def __init__(self, data) -> None:
        self.data = data
        self.index = 0

    def __iter__(self):
        """Retorna un iterador, i.e. implementa __next__"""
        return self

    def __next__(self):
        if self.index < len(self.data):
            element = self.data[self.index]
            self.index += 1
            return element
        else:
            raise StopIteration


# entry point
if __name__ == '__main__':

    # ejemplo 1,
    mi_coleccion = MiIterable([i for i in range(1, 11)])
    for item in mi_coleccion:
        print(item, end=', ')
    print()

    # ejemplo 2,
    nombres = ['jake', 'petter', 'mpho']

    # creamos iteradir
    name_iterator1 = iter(nombres)

    # accdemos a los nombres
    n1 = next(name_iterator1)
    n2 = next(name_iterator1)
    n3 = next(name_iterator1)
    print(n1, n2, n3)

    # creamos otro iterador
    name_iterator2 = iter(nombres)
    while True:
        try:
            print(next(name_iterator2), end=' ')
        except:
            print()
            break
