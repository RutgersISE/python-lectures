import numpy as np
import cv2

def color_mask(image, lower, upper):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
    mask = cv2.dilate(mask, kernel=(5, 5))
    return mask

if __name__ == "__main__":
    image = cv2.imread("yellow_blocks.jpg")
    image = cv2.resize(image, (0, 0), fx=.25, fy=.25)
    lower = [20, 50, 50]
    upper = [50, 255, 255]
    mask = color_mask(image, lower, upper)

    cv2.imshow("mask", mask)
    cv2.waitKey(0)