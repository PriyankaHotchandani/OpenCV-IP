import cv2
import numpy as np

main_image = cv2.imread('3D-Matplotlib.png')
logo = cv2.imread('mainlogo.png')

rows, cols, channels = logo.shape
roi = main_image[0:rows, 0:cols]

logo_grayscale = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(logo_grayscale, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

logo_fg = cv2.bitwise_and(logo, logo, mask=mask)
main_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

dst = cv2.add(logo_fg, main_bg)
main_image[0:rows, 0:cols] = dst

cv2.imshow('main', main_image)
cv2.imshow('logo', logo)
cv2.imshow('roi', roi)
cv2.imshow('gray', logo_grayscale)
cv2.imshow('mask', mask)
cv2.imshow('logo fg', logo_fg)
cv2.imshow('mask inv', mask_inv)
cv2.imshow('main bg', main_bg)
cv2.imshow('dst', dst)
cv2.imshow('final', main_image)

cv2.waitKey(0)
cv2.destroyAllWindows