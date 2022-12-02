import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('input_image_ex2.jpg')

image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,3,5)
ret, th1 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.dilate(th1,kernel,iterations = 1)

contours, hierarchy = cv2.findContours(image=th1, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

image_copy = img.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 255), thickness=5, lineType=cv2.LINE_AA)

# image_copy3 = image.copy()
# for i, contour in enumerate(contours):
#    for j, contour_point in enumerate(contour): 
#        cv2.rectangle(image_copy3, (contour_point[0][0],contour_point[0][0]), (contour_point[0][1], contour_point[0][1]), (255, 0, 0),2)


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
