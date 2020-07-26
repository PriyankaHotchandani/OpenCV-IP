import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    #Take each frame of the video
    ret, frame = cap.read()

    #Convert from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Define range of color in HSV
    lower_blue = np.array([0,0,0])
    upper_blue = np.array([180,255,255])

    #Create a mask for the specified range (Threshold HSV to get only blue)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    #Run a bitwise operation to restore the color (Bitwise AND mask and original frame)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('hsv',hsv)


    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release
cv2.destroyAllWindows