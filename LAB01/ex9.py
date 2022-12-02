##9 Create Border around Images

import cv2
import putText

img = cv2.imread("lena.png")

putText.putText(img, 'Exercise9')

image1 = cv2.copyMakeBorder(img, 5, 5, 5, 5, cv2.BORDER_CONSTANT, None, value = 0)
image2 = cv2.copyMakeBorder(img, 70, 70, 30, 30, cv2.BORDER_REFLECT)

cv2.imshow("CONSTANT", image1)
cv2.imwrite('image_9(1).jpg',image1)

cv2.imshow("REFLECT", image2)
cv2.imwrite('image_9(2).jpg',image2)

cv2.waitKey(0)
cv2.destroyAllWindows()

