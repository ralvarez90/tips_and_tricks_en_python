# -*- coding: utf-8 -*-

"""CREACIÓN DE CLASES DINÁMICAS CON TYPE

La función type se usa generalmente para saber el tipo de
dato de un objeto. Sin embargo también podemos usarla para
crear clases dinámicas.

Estas clases se crean en tiempo de ejecución."""


class Car:

    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color

    def description(self) -> str:
        return f'The car is {self.name} and its {self.color} in color'


def car_init(self, name: str, color: str):
    self.name = name
    self.color = color


# run example
if __name__ == '__main__':

    # uso directo
    print('Ejemplo 1, usando clase directa...')
    car1 = Car('bmw-zw', 'red')
    print(car1.description(), end='\n'*2)

    # creamos clase dinamica para su posterior uso
    Automovil = type('Automovil', (), {
        '__init__': car_init,
        'description': lambda self: f'El auto es {self.name} y es color {self.color}'
    })

    print('Ejemplo 2, clase dinamica con type')
    car2 = Automovil('Nissan-Z4', 'Negro')
    print(car2.description())
