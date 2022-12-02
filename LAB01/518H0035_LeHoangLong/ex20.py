## Draw a text string

import cv2
import putText
im = cv2.imread("lena.png")

putText.putText(im, 'Exercise20')


cv2.imshow("First window", im)
cv2.imwrite('image_20.jpg',im)
cv2.waitKey(0)
cv2.destroyAllWindows()