# -*- coding: utf-8 -*-

"""DICCIONARIOS POR COMPRENSIÓN

Al igual que otras secuencias, podemos generar diccionarios por comprensión,
es decir con una expresión un rango o iterable y condiciones."""

# original
dict1 = {'grade': 70, 'weight': 45, 'width': 89}
print(f'origin: {dict1}')

# valores de dict1 a flotantes
dict2 = {k: float(v) for k, v in dict1.items()}
print(f'dict2 : {dict2}')

# ejemplo 3
dict3 = {k: v/2 for (k, v) in dict1.items()}
print(f'dict3 : {dict3}')
