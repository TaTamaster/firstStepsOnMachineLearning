import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('/home/cesarxx/Imágenes/club-de-regatas-la-marina.jpg')
img2 = cv.imread('/home/cesarxx/Imágenes/1.jpg')

cv.imshow('yo', img2)
cv.imshow('Club de Regatas', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Crear la máscara
circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

# Aplicar la máscara a la imagen
masked_image = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Masked Image', masked_image)

# Calcular el histograma en escala de grises utilizando la máscara correcta
gray_hist = cv.calcHist([gray], [0], circle, [256], [0, 256])

# Graficar el histograma
plt.figure()
plt.title('Histograma en Escala de Grises')
plt.xlabel('Bins')
plt.ylabel('# de píxeles')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

cv.waitKey(0)