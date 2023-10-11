# -*- coding: utf-8 -*-
import sys

"""MEMORÍA Y __slots__

Se emplean dentro de las clases, y básicamente los elementos que
contengan serán variables de instancia.

En Python, __slots__ es una característica que permite limitar los 
atributos de una clase a un conjunto predefinido de nombres, lo que 
ahorra memoria y mejora el rendimiento. 

Al usar __slots__, puedes indicar a Python que solo permita un 
conjunto específico de atributos en una instancia de la clase y 
evite la creación dinámica de nuevos atributos. 

Esto puede ser útil en situaciones en las que deseas asegurarte de 
que una clase tenga solo ciertos atributos y deseas reducir el uso 
de memoria.

Para utilizar __slots__, debes definir una variable de clase llamada 
__slots__ en tu clase que contenga una lista de cadenas que representan 
los nombres de los atributos permitidos.

Los Python slots son una característica avanzada de Python que permite 
a los desarrolladores controlar la creación de atributos de instancia 
en una clase.

Consiste en asignarle __slots__ las variables con los nombres de los
atributos.
"""


class Car1:

    __slots__ = ['make', 'brand']

    def __init__(self, make: str, brand: str) -> None:
        self.make = make
        self.brand = brand


class Car2:

    def __init__(self, make: str, brand: str) -> None:
        self.make = make
        self.brand = brand


# entry point
if __name__ == '__main__':
    c1 = Car1('nissan', 'skyline')
    c2 = Car2('nissan', 'skyline')
    print(f'Car1 with size: {sys.getsizeof(c1)} bytes')
    print(f'Car2 with size: {sys.getsizeof(c2)} bytes')
