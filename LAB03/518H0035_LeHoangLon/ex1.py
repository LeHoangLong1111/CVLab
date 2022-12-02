
##1 Extracting the faces from the input image using a circular mask. Output is 3 of face images extracted from the input image.


import numpy as np
import cv2

image = cv2. imread('tem1.jpg')

cv2.imshow("First",image)
cv2.waitKey(0)

## First person 
mask = np.zeros(image.shape[:2], dtype="uint8")

cv2.circle(mask, (266, 398), 120, 255,-1)
cv2.imshow("Mask",image)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("First face", masked)
cv2.waitKey(0)

## Second person
cv2.circle(mask, (731, 307), 120, 255,-1)
cv2.imshow("Mask",image)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Second face", masked)
cv2.waitKey(0)

## third person
cv2.circle(mask, (1181, 454), 120, 255,-1)
cv2.imshow("Mask",image)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Third face", masked)
cv2.waitKey(0)
cv2.imwrite('image_1.jpg', masked)