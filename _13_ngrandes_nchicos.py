# -*- coding: utf-8 -*-
import heapq

"""RETORNO DE LOS PRIMEROS N MÁS GRANDES O LOS N MÁS PEQUEÑOS

Supongamos que tenemos una lista de m elementos, y queremos retornar
una lista que retorno los n elementos más grandes (o más pequeños).

Función sorted
Recibe un iterable y retorna una copia del mismo de forma ordenada.
Puede recibir una función key como criterio de ordenamiento, y
se puede asignar True o False al parámetro reverse.



Módulo heapq
Este módulo contiene el método nlargest y nsmallest."""


def get_n_largest_v1(items: list[int], n: int) -> list[int]:
    copy = sorted(items, reverse=True)
    return copy[:n]


def get_n_smallest_v1(items: list[int], n: int) -> list[int]:
    copy = sorted(items)
    return copy[:n]


# ejemplo 1, uso de sorted y slices de listas.
lista_enteros = [12, 34, 67, 98, 90, 68, 55, 54, 64, 35]
primeros_5_largos_v1 = get_n_largest_v1(lista_enteros, 5)
primeros_5_peques_v1 = get_n_smallest_v1(lista_enteros, 5)
print('primeros_5_largos_v1: {}'.format(primeros_5_largos_v1))
print('primeros_5_peques_v1: {}'.format(primeros_5_peques_v1))

# ejemplo 2, uso de heapq.
primeros_5_largos_v2 = heapq.nlargest(5, lista_enteros)
primeros_5_peques_v2 = heapq.nsmallest(5, lista_enteros)
print('primeros_5_largos_v2: {}'.format(primeros_5_largos_v2))
print('primeros_5_peques_v2: {}'.format(primeros_5_peques_v2))
