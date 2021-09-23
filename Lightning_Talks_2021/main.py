import numpy as np
import cv2 as cv
from functions import *

cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
# opencv_logo = cv.imread('samples/OpenCV_Logo.png')
face_cascade = cv.CascadeClassifier('samples/haarcascade_frontalcatface.xml')
lenna_img = cv.imread('samples/Lenna.png')

while True:
    # Capture frame by frame
    ret, frame = cap.read()
    frame_rz = cv.resize(frame, (640, 480))
    # print(frame_rz.shape)

    # b, g, r = split_by_copy(frame_rz)
    # b, g, r = cv.split(frame_rz)
    # cv.imshow('b', b)
    # cv.imshow('g', g)
    # cv.imshow('r', r)


    # thresh_frame = frame_rz.copy()
    # kernel = np.ones((1, 1), dtype=np.uint8)
    # gray = cv.cvtColor(thresh_frame, cv.COLOR_BGR2GRAY)
    #
    # blur = cv.blur(gray, (1, 1))
    #
    # gaussianBlur = cv.GaussianBlur(blur, (1, 1), 0)
    #
    # erosion = cv.erode(gaussianBlur, kernel, iterations=10)
    #
    # opening = cv.morphologyEx(erosion, cv.MORPH_OPEN, kernel)
    #
    # closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)
    #
    # dilated = cv.dilate(closing, None, iterations=2)
    #
    # ret, th1 = cv.threshold(dilated, 120, 255, cv.THRESH_BINARY)

    # cv.imshow('threshold', th1)

    # contours, _ = cv.findContours(th1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # cv.drawContours(thresh_frame, contours, -1, (0, 255, 0), 1)
    # cv.imshow('tresh_frame', thresh_frame)


    # face_frame = frame.copy()
    # faces = face_cascade.detectMultiScale(face_frame, 1.05, 5)
    # for (x, y, w, h) in faces:
    #     cv.rectangle(face_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # cv.imshow('face_detection', face_frame)



    cv.imshow('frame', frame_rz)
    if cv.waitKey(1) == 27:
        break

cap.release()
cv.destroyAllWindows()
