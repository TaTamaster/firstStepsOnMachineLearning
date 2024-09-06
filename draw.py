# import cv2

# cap = cv2.VideoCapture(0)  # Abre la cámara web

# while True:
#     ret, frame = cap.read()  # Lee un frame de la cámara
#     cv2.imshow('Video', frame)  # Muestra el frame en una ventana

#     if cv2.waitKey(1) == ord('q'):  # Si se presiona 'q', se sale del bucle
#         break

# cap.release()
# cv2.destroyAllWindows()
import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#img = cv.imread('/home/cesarxx/Imágenes/1.jpg')
#cv.imshow('1', img)
# 1. Paint the image a certain colour
# blank[200:300, 300:400] = 0,0 , 255
# cv.imshow('Red', blank)
# blank[:] = 0, 255, 0
# cv.imshow('Green', blank)

cv.rectangle(blank, (0, 0), (250, 250), (0,255,0), thickness=3)
cv.imshow('Rectangle', blank)

cv.waitKey(0)