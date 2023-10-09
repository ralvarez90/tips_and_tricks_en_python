# -+- coding: utf-8 -*-
import demoji

"""DE EMOGIS A TEXTO

Con la librería demogi podemos obtener un diccionario con todos los
emogis en texto. Los emogis son el key mientras que los valores son
el texto."""

some_text = 'Esto es un texto 😆 con emogis. Esto es una groseria 🖕 y esto mamadisimo 💪'
emojis_dict = demoji.findall(string=some_text)
print(emojis_dict)

