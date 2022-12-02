##1 Reading an image in OpenCV using Python
import cv2
import putText
im = cv2.imread("lena.png")

putText.putText(im, 'Exercise1')


cv2.imshow("First window", im)
cv2.imwrite('image_1.jpg',im)
cv2.waitKey(0)
cv2.destroyAllWindows()