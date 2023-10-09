# -*- coding: utf-8 -*-

"""RETURN VS YIELD

La sentencia return devuelve un elemento y finaliza la función, por
otro lado, la sentencia yield (producir, cosechar) retorna un
'paquete' de elementos llamado generador. Se requiere 'desempacar'
ese generador para obtener los elementos.

Puede emplear la función next dentro de un for para ir 
'desempacando' ese generador.

En otras palabra, una función con sentencia yield retorna un 
generador.

Los generadores se evalúan de forma perezosa, es decir, genera
o entrega valores/datos bajo demanda, es decir hasta el momento en
que se van a ocupar.

Otra forma de implementar generadores es por comprensión, y es de
la mismoa forma que las listas por comprensión pero usando
paréntesis.
"""


def numero_v1(n: int) -> int:
    for i in range(n):
        return i


def numero_v2(n: int):
    for i in range(n):
        yield i


def numero_v3(n: int):
    return (i for i in range(n))


# test, con sentencia return
print('Si n=5')
print(numero_v1(n=5))

# obtenemos generdores
some_generator1 = numero_v2(5)
some_generator2 = numero_v3(5)

# desempacamos generadores
for i in some_generator1:
    print(i, end=' ')
print('\n' + '-'*30)

for i in some_generator2:
    print(i, end=' ')
print('\n' + '-'*30)
