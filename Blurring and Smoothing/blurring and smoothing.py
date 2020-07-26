import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    

    lower_blue = np.array([10,34,78])
    upper_blue = np.array([180,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((15,15),np.float32)/225
    smoothed = cv2.filter2D(res,-1,kernel)

    blur = cv2.GaussianBlur(res,(15,15),0)
    median = cv2.medianBlur(res,15)
    bilateral = cv2.bilateralFilter(res,15,75,75)


    cv2.imshow('smoothed',smoothed)
    cv2.imshow('blur gaussian',blur)
    cv2.imshow('blur median',median)
    cv2.imshow('blur bilateral',bilateral)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release
cv2.destroyAllWindows