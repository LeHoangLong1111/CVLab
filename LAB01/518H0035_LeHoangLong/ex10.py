## 10. Grayscaling of Images
import cv2

img = cv2.imread('lena.png')
cv2.imshow('First', img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Second', gray)
cv2.imwrite('image_10.jpg',gray)
cv2.waitKey(0)

cv2.destroyAllWindows()