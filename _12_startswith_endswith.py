# -*- coding: utf-8 -*-

"""MÉTODOS STARTSWITH Y ENDSWITH

Los métodos de striggs startswith y endswith retornan booleanos
que indican si un string inicia o finaliza con el prefijo o
sufijo indicado."""

some_words = ['lemon', 'apple', 'orange', 'apricot', 'bananna']
inicio_con_a = [w for w in some_words if w.startswith('a')]
fin_con_a = [w for w in some_words if w.endswith('a')]
print('some_words  : {}'.format(some_words))
print('inicio_con_a: {}'.format(inicio_con_a))
print('fin_con_a   : {}'.format(fin_con_a))
