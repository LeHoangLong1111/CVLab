import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku-original.jpg', 0)

th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,3,5)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,3,5)
ret, th3 = cv2.threshold(img,127, 255, cv2.THRESH_BINARY)

titles = ['Original Image', 'Adaptive Thresh Mean', 'Adaptive Thresh Gaussian', 'Threshold']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
cv2.imwrite('pic1_1.jpg',th1)
cv2.imwrite('pic1_2.jpg',th2)
cv2.imwrite('pic1_3.jpg',th3)