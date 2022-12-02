## Visualizing image in different color spaces
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena.png')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
img4 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img5 = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
plt.imshow(img, cmap ='hot') 
plt.imshow(img, cmap ='nipy_spectral')

cv2.imshow('Original', img)
cv2.imwrite('image_14(1).jpg',img)
cv2.waitKey(0)         
cv2.destroyAllWindows()

cv2.imshow('Gray', img2) 
cv2.imwrite('image_14(2).jpg',img2)
cv2.waitKey(0)         
cv2.destroyAllWindows()

cv2.imshow('HSV', img3)
cv2.imwrite('image_14(3).jpg',img3)
cv2.waitKey(0)         
cv2.destroyAllWindows()

cv2.imshow('HSV', img4)
cv2.imwrite('image_14(4).jpg',img4)
cv2.waitKey(0)         
cv2.destroyAllWindows()

cv2.imshow('LAB', img5)
cv2.imwrite('image_14(5).jpg',img5)
cv2.waitKey(0)         
cv2.destroyAllWindows()

cv2.imshow('LABlacian', laplacian)
cv2.imwrite('image_14(6).jpg',laplacian)
cv2.waitKey(0)         
cv2.destroyAllWindows()