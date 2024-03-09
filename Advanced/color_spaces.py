import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('./Resources/Photos/boston.jpg')
cv.imshow('Boston', img)  # READS IMAGE IN BGR

plt.imshow(img) # READS IMAGE IN RGB
plt.show()

#BGR TO GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR TO HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR TO LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

#BRG TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb", rgb)

cv.waitKey(0)