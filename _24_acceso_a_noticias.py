# -*- coding: utf-8 -*-
from newspaper import Article

"""OBTENER NOTICIAS EN PYTHON

Instalando el paquete newspaper3k podemos escrapear noticias en la web. Se
requiere el link de un artículo."""

articulo_nvidia = Article(("https://indianexpress.com/article/"
                           "technology/gadgets/"
                           "apple-discontinues-its-last-ipod-model-7910720/"))

# descargamos
articulo_nvidia.download()
articulo_nvidia.parse()
print(articulo_nvidia.text)
print(f'Dia de publicación: {articulo_nvidia.publish_date}')
