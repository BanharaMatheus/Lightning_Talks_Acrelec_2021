import cv2 as cv
import numpy as np


def split_by_copy(frame_input):
    blue_channel = frame_input.copy()
    # set green and red channels to 0
    blue_channel[:, :, 1] = 0
    blue_channel[:, :, 2] = 0

    green_channel = frame_input.copy()
    # set blue and red channels to 0
    green_channel[:, :, 0] = 0
    green_channel[:, :, 2] = 0

    red_channel = frame_input.copy()
    # set blue and green channels to 0
    red_channel[:, :, 0] = 0
    red_channel[:, :, 1] = 0

    return blue_channel, green_channel, red_channel


def draw_function(frame_input):
    img = frame_input.copy()
    cv.circle(img, (330, 200), 20, (255, 255, 255), -1)  # Desenhando o círculo
    cv.line(img, (0, 0), (511, 511), (0, 255, 0), 5)
    cv.rectangle(img, (0, 250), (200, 128), (10, 150, 255), -1)
    cv.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 3)
    cv.ellipse(img, (120, 400), (100, 50), 0, 0, 360, 255, -1)

    pts = np.array([[350, 250], [500, 275], [280, 400], [630, 460], [600, 150]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv.polylines(img, [pts], False, (0, 255, 255), 2)

    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, 'Acrelec', (30, 100), font, 4, (255, 255, 255), 2, cv.LINE_AA)

    return img
