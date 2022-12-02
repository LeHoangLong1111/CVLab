##2 Blend the following 2 images to create a new image

import numpy as np
import cv2

image = cv2. imread('tem1.jpg')

image_logo = cv2.imread('logo.png')

# # print(image_logo.shape)
# cv2.imshow("Third face", image_logo)
# cv2.waitKey(0)

width = int(image.shape[1] * (100) / 100)
height = int(image.shape[0] * (100) / 100)
dim=(width, height)

# print(dim)

image_logo_resize = cv2.resize(image_logo, dim)

dst = cv2.addWeighted(image, 0.5, image_logo_resize, 0.5, 0)

cv2.imshow("Result",dst)
cv2.waitKey(0)
cv2.imwrite('image_2.jpg', dst)