# -*- coding: utf-8 -*-
import speedtest

"""VERIFICAR VELOCIDAD DE INTERNET

El módulo speedtest se puede emplear para verificar la velocidad
de su internet.

Este módulo no viene incluido en la librería standard por lo que
se requiere de instalar.

pip install speedtest-cli
"""

speed = speedtest.Speedtest()
print('Subida : {:.2f} MB'.format(speed.upload()/8_000_000))
print('Bajada : {:.2f} MB'.format(speed.download()/8_000_000))
