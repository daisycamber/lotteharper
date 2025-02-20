from imutils import paths
import argparse
import cv2
import sys

def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

def detect_blur(imagePath):
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
    # check image quality
    print('Variance of laplacian is ' + str(fm))
    if fm < 7:
        return True
    return False
