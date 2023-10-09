# -*- coding: utf-8 -*-
import PyPDF2

"""EXTRAER TEXTO DE PDFs

Empleando la librería PyPDF2 podemos extaer texto
de un pdf.

La instalación se realiza con 
pip install PyPDF2

Empleamos PdfFileReader
"""

# open file
pdf_file = open(file='Python Tips and Tricks.pdf', mode='rb')

# read pdf reader
read_file = PyPDF2.PdfReader(pdf_file)

# leemos página específica (4)
pagina_reviews = read_file.pages[4]

# extraemos
print(pagina_reviews.extract_text())

# cerramos archivo
pdf_file.close()
