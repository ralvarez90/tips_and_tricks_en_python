# -*- coding: utf-8 -*-
from pdf2docx import Converter

"""CONVERSOR DE PDFs A ARCHIVOS DE WORD

Se requiere instalar la dependencia pdf2docx ejecutando
pip install pdf2docx 

Empleando la clase Converter del módulo pdf2docx.
"""

pdf_file = 'Python Tips and Tricks.pdf'
word_file = 'python_tips_and_tricks.docx'

# instancia de convertidor
cv = Converter(pdf_file)
cv.convert(word_file)

cv.close()
