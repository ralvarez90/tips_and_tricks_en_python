# -*- coding: utf-8 -*-
import cv2 as cv

"""CONVERTIR IMAGEN A SCALA DE GRISES

1. Instalamos dependencias
pip install opencv-python"""

# leemos imagen
img_original = cv.imread('gopher.png')

# mostramos imagen original por un lapso
cv.imshow('Original', img_original)
cv.waitKey(5000)

# convertimos a imagen gris
img_gray = cv.cvtColor(img_original, code=cv.COLOR_BGR2GRAY)
cv.imshow('Gray', img_gray)
cv.waitKey(5000)

# salvamos imagen
cv.imwrite('gray_gopher.png', img_gray)
