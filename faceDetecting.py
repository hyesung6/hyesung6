import cv2 as cv

def getMask(rect1, rect2):
    (x1, y1, w1, h1) = rect1
    (x2, y2, w2, h2) = rect2


    # Read image from your local file system
# original_image = cv.imread('D:\\Account4Windows10\\Desktop\\faceImage.jpg')
# original_image = cv.imread('D:/Account4Windows10/Desktop/faceImage.jpg')
original_image = cv.imread('D:/Account4Windows10/Desktop/faceImage2.jpg')
cv.imshow("original", original_image)

# Convert color image to grayscale for Viola-Jones
grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
cv.imshow("gray...", grayscale_image)

# Load the classifier and create a cascade object for face detection
# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt2.xml
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
#face_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
#face_cascade = cv.CascadeClassifier('https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt2.xml')
detected_eyes = eye_cascade.detectMultiScale(grayscale_image, scaleFactor=1.05, minNeighbors=7)
detected_faces = face_cascade.detectMultiScale(grayscale_image, scaleFactor=1.1, minNeighbors=5)
for (x1, y1, width, height) in detected_faces:
    rect = cv.rectangle(
        original_image,
        (x1, y1),
        (x1 + width, y1 + height),
        (0, 255, 0),  #BGR
        2
    )

cv.imshow('Image', original_image)
cv.waitKey(0)
cv.destroyAllWindows()