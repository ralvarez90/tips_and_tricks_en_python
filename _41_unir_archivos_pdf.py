# -*- coding: utf-8 -*-
import os
from PyPDF2 import PdfFileMerger, PdfFileReader

"""UNIER/MEZCLAR ARCHIVOS PDF

Instalando la librería PyPDF2, podemos mezclar una cantidad
de archivos en pdf.

Se instala la dependencia con:
pip install pyPDF2

Los pdfs que desea unir deben ubicrase en el mismo directorio
en el que se ejecuta el script de python.
"""

# lista de pdfs a unir
pdfs_to_join = ['file1.pdf', 'file2.pdf']
for pdf in pdfs_to_join:
    if not os.path.exists(pdf):
        raise ValueError(f'No existe el pdf {pdf}')

# mezcla de pdfs
merge = PdfFileMerger(strict=True)
