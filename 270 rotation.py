import cv2
import numpy as np
image = cv2.imread("C:/Users/KUSUMA PRIYA/Desktop/picture 10.png")
if image is None:
    print("Error: Unable to load the image.")
else:
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow('Original Image', image)
    cv2.imshow('Rotated Image (270 degrees)', rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
