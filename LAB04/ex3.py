import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('ex3.png')

image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, th1 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)

opening = cv2.morphologyEx(th1, cv2.MORPH_OPEN, kernel)

losing = cv2.morphologyEx(th1, cv2.MORPH_CLOSE, kernel)

erosion = cv2.dilate(opening,kernel,iterations = 1)

contours, hierarchy = cv2.findContours(image=th1, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

image_copy = img.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 255), thickness=5, lineType=cv2.LINE_AA)


idx = 0 
for cnt in contours:
    idx += 1
    x,y,w,h = cv2.boundingRect(cnt)
    roi = image[y:y+h,x:x+w]
    cv2.rectangle(image_copy,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow('Result', image_copy)
cv2.waitKey(0)
cv2.imwrite('pic2.jpg', image_copy)
cv2.destroyAllWindows()
