import cv2 as cv
import numpy as np

img = cv.imread('./Resources/Photos/park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype ='uint8')

b, g, r = cv.split(img) # SPLITS THE IMAGE INTO RESPECTIVE COLOR CHANNELS

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

# merge the above seperate color channel into one
merged = cv.merge([b, g, r])
cv.imshow('Merged image', merged)

cv.waitKey(0)