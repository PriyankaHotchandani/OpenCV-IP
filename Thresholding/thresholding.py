import cv2
import numpy as np 

img = cv2.imread('bookpage.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret1, thresh1 = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
ret2, thresh2 = cv2.threshold(img_gray, 12, 255, cv2.THRESH_BINARY)
ret3, thresh3 = cv2.threshold(img_gray, 12, 255, cv2.THRESH_BINARY_INV)
thresh4 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
ret, thresh5 = cv2.threshold(img_gray, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('thresh1',thresh1)
cv2.imshow('thresh2',thresh2)
cv2.imshow('thresh3',thresh3)
cv2.imshow('thresh4',thresh4)
cv2.imshow('thresh5',ret)

cv2.waitKey(0)
cv2.destroyAllWindows