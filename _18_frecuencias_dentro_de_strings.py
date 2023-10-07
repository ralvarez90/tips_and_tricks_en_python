# -*- coding: utf-8 -*-
import collections

"""FRECUENCIAS DENTRO DE UN STRING

Podemos obtener el caracter más frecuente de un string
empleando la función max y la función de strings count.

Por otro lado, recordemos que el método
collections.Counter(items).most_common() podemos obtener tuplas
que indican los n elementos más comunes.
"""

# string a prueba
message = 'fecklessness'

# forma 1, metodo max
most_frequent_v1 = max(message, key=message.count)
print('Most frecuente: {}'.format(most_frequent_v1))

# forma 2, método Counter().most_common
most_frequent_v2 = collections.Counter(message).most_common(1)
print('Most frecuente: {}'.format(most_frequent_v2))
