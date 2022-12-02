##6 Arithmetic operations on Images

import cv2
import numpy as np
import putText

image1 = cv2.imread('pic1.jpg')
image2 = cv2.imread('pic2.jpg')

weightedSum=cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
putText.putText(weightedSum, 'Exercise6 Sum')
sub = cv2.subtract(image1, image2)
putText.putText(sub, 'Exercise6 Sub')

cv2.imshow('Weighted Image', weightedSum)
cv2.imwrite('image_6(1).jpg',weightedSum)

cv2.imshow('Subtracted Image', sub)
cv2.imwrite('image_6(2).jpg',sub)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()