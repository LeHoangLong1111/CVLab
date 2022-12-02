import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('pic.jpg', 0)
histr = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(histr)
plt.show()

equ=cv2.equalizeHist(img)
result=np.hstack((img, equ))
histr2 = cv2.calcHist([result],[0],None,[256],[0,256])
cv2.imwrite('pic1.jpg',result)
# plt.plot(histr2)
# plt.show()
# plt.plot(histr2)
# plt.show()
# cv2.imshow('Result', result)
# cv2.waitKey(0)
