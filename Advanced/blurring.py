import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Park', img)

# Averaging 
avg = cv.blur(img, (3,3))
cv.imshow('Average Blur', avg)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gaussian)

#Medium blur
median = cv.medianBlur(img, 3)
cv.imshow('Median blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 24)
cv.imshow('Bilateral img', bilateral)


cv.waitKey(0)