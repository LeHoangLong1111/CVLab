##2 Display an image in OpenCV using Python
import cv2
import putText
im = cv2.imread("lena.png", 0)

putText.putText(im, 'Exercise2')

cv2.imshow("Ex2", im)
cv2.imwrite('image_2.jpg',im)
cv2.waitKey(0)
cv2.destroyAllWindows()