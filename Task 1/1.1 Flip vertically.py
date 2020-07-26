import cv2
import numpy as np

cap = cv2.VideoCapture(0)
count = 0
def count_frames(count):
        if count % 2 !=0:
            cv2.imshow('flipped',flipVert)
        else:
            cv2.imshow('flipped',frame)


while True:
    ret, frame = cap.read()
    flipVert = cv2.flip(frame, 0)
    count=count+1

    count_frames(count)
   
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()

#out.release()
cv2.destroyAllWindows()    