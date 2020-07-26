import cv2
import numpy as np 

img_1 = cv2.imread('3D-Matplotlib.png')
img_2 = cv2.imread('pythonblack.jpg')

rows, columns, channels = img_2.shape
#img_2 = cv2.addWeighted(img_1[0:rows, 0:columns], 0.5, img_2, 0.5, 0)
#img_1[0:rows, 0:columns] = img_2
roi = img_1[0:rows, 0:columns] 

img_2gray = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img_2gray, 80, 255, cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

img_1bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img_2fg = cv2.bitwise_and(img_2, img_2, mask=mask)

dst = cv2.add(img_1bg, img_2fg)
img_1[0:rows, 0:columns] = dst

cv2.imshow('img', img_1)
#cv2.imshow('imgg', img_2fg)
#cv2.imshow('imggg', mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows