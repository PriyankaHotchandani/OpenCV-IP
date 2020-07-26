import cv2
import numpy as np

cap = cv2.VideoCapture(0)
count = 0
def count_frames(count):
    if count % 2 !=0:
        cv2.imshow('window',cropped)
    else:
        cv2.imshow('window',frame)

while True:
    ret, frame = cap.read()
    cropped = frame[295:345, 215:265]
    frame[0:50, 0:50] = cropped
    count=count+1

    count_frames(count)

    if cv2.waitKey(77) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    