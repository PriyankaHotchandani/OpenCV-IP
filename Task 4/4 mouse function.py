import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def mouse(event,x,y,flags,params):
    print(frame[y,x])

cv2.namedWindow('Frame')
cv2.setMouseCallback("Frame",mouse)

while True:
    ret,frame = cap.read()
    cv2.imshow('Frame',frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows
cap.release