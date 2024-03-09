import cv2 as cv

img = cv.imread('../Resources/Photos/group 1.jpg')
#cv.imshow('Group of peoples', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("Gray scale", gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

face_detect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=1)

print(f'Number of faces found = {len(face_detect)}')

for(x, y, w, h) in face_detect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Detected faces', img)

cv.waitKey(0)