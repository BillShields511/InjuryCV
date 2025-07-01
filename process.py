import cv2
import numpy as np

def process_image(image, threshold1=50, threshold2=150):
    """
    Process the image to detect edges
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, threshold1, threshold2)
    return edges

img = cv2.imread('raw_images/cuts/raw-cut-1.png')
processed_img = process_image(img, 100, 200)
processed_img2 = process_image(img, 50, 150)

cv2.imshow('Edges', processed_img)
cv2.imshow('Edges2', processed_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

