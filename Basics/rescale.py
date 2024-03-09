import cv2 as cv

img = cv.imread('./Resources/Photos/cat_large.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale = 0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # only applied on Live video
    cv.set(3, width)
    cv.set(4, height)

resized_image = rescaleFrame(img, 0.25)
cv.imshow('Image', resized_image)

cv.waitKey(0)