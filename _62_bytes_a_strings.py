# -*- coding: utf-8 -*-

"""De bytes a string

Un objeto de tipo bytes es una secuencia inmutable de bytes. Representa una
secuencia de datos binarios, por lo que puede contener valores enteros en el
rango de 0 a 255.

Podemos generar estos con:
- literales de bytes
- constructor bytes

Para obtener un objeto bytes a partir de un string podemos emplear la función
str(objeto_bytes, encoding='utf-8')  o la función decode de las instancias de
bytes.

Nota:
- Podemos obtener una instancia de bytes a partir de un string empleando el
método encode() de los strings
"""

# literal de bytes
instancia_de_bytes1 = b'Hello'
print(f'{instancia_de_bytes1} with type {type(instancia_de_bytes1)}')

# con constructor
instancia_de_bytes2 = bytes([72, 101, 108, 108, 111])
print(f'{instancia_de_bytes2} with type {type(instancia_de_bytes2)}')

# de bytes a string, forma 1
str_from_bytes1 = str(instancia_de_bytes1, encoding='utf-8')
print(str_from_bytes1)

# de bytes a string, forma 2
str_from_bytes2 = instancia_de_bytes2.decode()
print(str_from_bytes2)

# de string a bytes, forma 1
print('Saludos a todos'.encode())

# de string a bytes, forma 2
print(bytes('Saludos a todos', encoding='utf-8'))
