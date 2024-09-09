import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('/home/cesarxx/Imágenes/club-de-regatas-la-marina.jpg')

cv.imshow('Club de Regatas', img)

# plt.imshow(img)
# plt.show()

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('In Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('Using HSV Colors', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_bgr)

# HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB to BGR', lab_bgr)

plt.imshow(rgb)
plt.title('Imagen con círculo')
plt.show()

cv.waitKey(0)