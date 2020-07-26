import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow('track')

def callback(x):
    pass

cv2.createTrackbar('H (lower)', 'track', 0, 180, callback)
cv2.createTrackbar('H (higher)', 'track', 180, 180, callback)
cv2.createTrackbar('S (lower)', 'track', 0, 255, callback)
cv2.createTrackbar('S (higher)', 'track', 255, 255, callback)
cv2.createTrackbar('V (lower)', 'track', 0, 255, callback)
cv2.createTrackbar('V (higher)', 'track', 255, 255, callback)


while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    

    hl = cv2.getTrackbarPos('H (lower)', 'track')
    hh = cv2.getTrackbarPos('H (higher)', 'track')
    sl = cv2.getTrackbarPos('S (lower)', 'track')
    sh = cv2.getTrackbarPos('S (higher)', 'track')
    vl = cv2.getTrackbarPos('V (lower)', 'track')
    vh = cv2.getTrackbarPos('V (higher)', 'track')

    lower_hsv = np.array([hl,sl,vl])
    upper_hsv = np.array([hh,sh,vh])

    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0,255,0), 2)
    #print(hierarchy)

    for c in contours:
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),2)

    
    cv2.imshow('track',res)
    cv2.imshow('mask',mask)
    cv2.imshow('hsv',res)
    cv2.imshow('thresh',thresh)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release
cv2.destroyAllWindows