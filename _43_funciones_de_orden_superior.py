# -*- coding: utf-8 -*-

"""FUNCIONES DE ORDEN SUPERIOR

Una HOF (High Order Function) es aquella que cumple al menos
una de las siguientes condiciones:
- Recibe alguna función como argumento
- Retorna una función
"""


def sort_names_criteria(name: str) -> str:
    """Retorna el primer elemento del nombre."""
    assert name, 'The name parameter cannot be empty string'
    return name[0]


# lista de tuplas
names = [
    ('John', 'Kely'),
    ('Chris', 'Rock'),
    ('Will', 'Smith'),
]

# lista de tuplas ordenads
sorted_names_v1 = sorted(names, key=sort_names_criteria)
sorted_names_v2 = sorted(names, key=lambda x: x[0])

# resultados
print(f'original_names: {names}')
print(f'sorted_names_v1  : {sorted_names_v1}')
print(f'sorted_names_v2  : {sorted_names_v2}')