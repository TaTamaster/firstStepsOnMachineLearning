import cv2 as cv
import numpy as np

img = cv.imread('/home/cesarxx/Imágenes/club-de-regatas-la-marina.jpg')

cv.imshow('Club de Regatas', img)

# Create a blank image

blank = np.zeros(img.shape[:2], dtype='uint8')

# Splitting the image into its channels
b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r]) 

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)

# print(img.shape)    # (1080, 1920, 3)
# print(b.shape)      # (1080, 1920)

cv.waitKey(0)
