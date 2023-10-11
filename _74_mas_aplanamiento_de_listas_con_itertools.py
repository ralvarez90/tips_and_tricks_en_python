# -*- coding: utf-8 -*-
import more_itertools

"""APLANAMIENTO DE LISTAS

Existen diversar formas de aplanar listas anidadas, otra forma es
empleando la librería more_itertools y emplear su respectivo método
collapse.

La ventaja de collapse es que permite aplanar listas anidadas y tuplas
anidadas.
"""

anidada1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
anidada2 = [(12, 34, 23), (1, 2, 3, 4), (1, 2)]
print(list(more_itertools.collapse(anidada1)))
print(list(more_itertools.collapse(anidada2)))
