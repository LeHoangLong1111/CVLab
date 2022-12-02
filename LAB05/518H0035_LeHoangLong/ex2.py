import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('pic.jpg', 0)
noise = np.zeros(img.shape)
cv2.randu(noise, 0, 256)
noisy_gray = img+ np.array(0.2*noise, dtype=np.float)
cv2.imwrite('pic2_1.jpg',noisy_gray)

## Averaging image using built-in functions in OpenCV
img_blur = cv2.blur(src=img, ksize=(5,5))
cv2.imwrite('pic2_2.jpg',img_blur)


## Gaussian Blurring
gaussian_blur = cv2.GaussianBlur(src=img, ksize=(5,5), sigmaX=0, sigmaY=0)
cv2.imwrite('pic2_3.jpg',gaussian_blur)

## Median Blurring
median = cv2.medianBlur(src=img, ksize=5)
cv2.imwrite('pic2_4.jpg',median)

##Bilateral Filtering
bilateral = cv2.bilateralFilter(src=img, d=9, sigmaColor=75, sigmaSpace=75)
cv2.imwrite('pic2_5.jpg',bilateral)

# Using a Custom 2D-Convolution Kernel
kernel2 = np.ones((5, 5), np.float32) / 25
kernel_blur = cv2.filter2D(img, -1, kernel2)
cv2.imwrite('pic2_6.jpg',kernel_blur)
# cv2.imshow('Result', kernel_blur)
# cv2.waitKey(0)