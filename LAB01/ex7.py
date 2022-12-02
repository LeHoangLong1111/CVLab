##7 Bitwise Operations on Binary Images

import cv2
import numpy as np
import putText

img1 = cv2.imread('pic7_1.png')
img2 = cv2.imread('pic7_2.png')

out_and = cv2.bitwise_and(img1, img2, mask=None)
putText.putText(out_and, 'Ex7 with AND')

out_or = cv2.bitwise_or(img1, img2, mask=None)
putText.putText(out_or, 'Ex7 with OR')

out_xor = cv2.bitwise_xor(img1, img2, mask=None)
putText.putText(out_xor, 'Ex7 with XOR')

out_not1= cv2.bitwise_not(img1, mask=None)
putText.putText(out_not1, 'Ex7 with NOT Pic1')

cv2.imshow('Bitwise AND', out_and)
cv2.imwrite('image_7(1).jpg',out_and)
cv2.imshow('Bitwise OR', out_or)
cv2.imwrite('image_7(2).jpg',out_or)
cv2.imshow('Bitwise XOR', out_xor)
cv2.imwrite('image_7(3).jpg',out_xor)
cv2.imshow('Bitwise NOT', out_not1)
cv2.imwrite('image_7(4).jpg',out_not1)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()