import cv2 as cv

#img = cv.imread('/home/cesarxx/Imágenes/1.jpg')

#cv.imshow('1', img)

capture = cv.VideoCapture('/home/cesarxx/Vídeos/Video.mp4')

while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

#cv.waitKey(0)