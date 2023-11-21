import cv2
import numpy as np
image_path = "C:/Users/KUSUMA PRIYA/Desktop/picture 7.jpg" 
original_image = cv2.imread(image_path)
height, width = original_image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), -90, 1)
rotated_image = cv2.warpAffine(original_image, rotation_matrix, (width, height))
cv2.imshow('Original Image', original_image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
