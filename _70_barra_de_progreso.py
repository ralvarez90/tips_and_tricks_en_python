# -*- coding: utf-8 -*-
from tqdm import tqdm
from time import sleep

"""BARRA DE PROGRESO

Con la librería tqdm podemos mostrar barras de progreso. Esta
librería crea un medidpr de progreso trackea al proceso del su loop."""

for i in tqdm(range(100_000), desc='snap packages'):
    sleep(1e-6)
