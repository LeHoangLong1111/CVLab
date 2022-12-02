##12 Convert an image from one color space to another

import cv2

path = r"lena.png"

src = cv2.imread(path)

image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV )
image2 = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY )
image3 = cv2.cvtColor(src, cv2.COLOR_RGB2RGBA )

cv2.imshow("HSV", image)
cv2.imwrite('image_12(1).jpg',image)
cv2.waitKey(0)
cv2.imshow("Gray", image2)
cv2.imwrite('image_12(2).jpg',image2)
cv2.waitKey(0)
cv2.imshow("RGB", image3)
cv2.imwrite('image_12(3).jpg',image3)
cv2.waitKey(0)