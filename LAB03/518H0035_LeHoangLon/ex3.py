import numpy as np
import cv2

image = cv2. imread('temp3.PNG', cv2.IMREAD_GRAYSCALE)

##1 Convert the image into 02 binary images, that numbers greater than or equals to 180 are in black, and numbers less than 180 are in white.

th, dst = cv2.threshold(image, 180, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Result 3_1",dst)
cv2.waitKey(0)
cv2.imwrite('image_3_1.jpg', dst)
# masked = cv2.bitwise_not(image)
# cv2.imshow("abc",masked)
# cv2.waitKey(0)
th, dst1 = cv2.threshold(image, 180, 255, cv2.THRESH_BINARY)
dst=cv2.bitwise_not(dst)   
masked = cv2.bitwise_and(image, dst)
masked2 = cv2.bitwise_xor(image, masked)
# result = cv2.bitwise_not(masked)
cv2.imshow("image_3_2",masked2)
cv2.imwrite('image_3_2.jpg', masked)
cv2.waitKey(0)
 