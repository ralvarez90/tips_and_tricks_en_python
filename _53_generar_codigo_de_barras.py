# -*- coding: utf-8 -*-
from barcode import ISBN13
from barcode.writer import ImageWriter
from PIL import Image

"""GENERAR CÓDIGOS DE BARRAS

Con la librería python-barcode podemos crear códigos de barras."""

cell_number = '979117528719'

# saving image as png
bar_code = ISBN13(cell_number, writer=ImageWriter())
bar_code.save('bar_code')

# read the image using pillow
img = Image.open('bar_code.png')
img.show()
