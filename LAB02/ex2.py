##8 Increase the brightness of the image
import numpy as np
import cv2

image = cv2. imread('poro.jpg')
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
value = 100
image_hsv[:,:,2] += value
result = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)
# cv2.imshow('image_2_8', result)
# cv2.waitKey(0)
cv2.imwrite('image_2_8.jpg', result)

##9 Enhance the image contrast by using global histogram equalization
image = cv2. imread('poro.jpg',0 )
equ=cv2.equalizeHist(image)
result9=np.hstack((image, equ))
cv2.imwrite('image_2_9.jpg', result9)

##10 Enhance the image contrast by using adaptive histogram equalization (CLHE)
image = cv2. imread('image_2_8.jpg', 0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1=clahe.apply(image)
# cv2.imshow('image_2_9', cl1)
# cv2.waitKey(0)
cv2.imwrite('image_2_10.jpg', cl1)
