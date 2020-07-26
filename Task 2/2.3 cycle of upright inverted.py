import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
start_time = time.time()

while True:
    ret, frame = cap.read()
    cv2.imshow('window',frame)
    flipVert = cv2.flip(frame, 0)
    current_time = time.time()
    #print (int(current_time)-int(start_time))
    if (int(current_time) - int(start_time))%5 == 0:
        cv2.imshow('window', flipVert)
    else :
        cv2.imshow('window', frame)


    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    