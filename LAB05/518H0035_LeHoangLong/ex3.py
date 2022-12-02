import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('pic.jpg', cv2.IMREAD_COLOR)

kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
image_sharp = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
cv2.imwrite('pic3_1.jpg', image_sharp)


gauss = cv2.GaussianBlur(img, ksize=(5,5), sigmaX=0, sigmaY=0)
sharp = cv2.addWeighted(img, 1.5, gauss, -0.5, 0)
cv2.imwrite('pic3_2.jpg', sharp)
# cv2.imshow('Result', image_sharp)
# cv2.waitKey(0)

