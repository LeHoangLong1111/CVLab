import cv2
import numpy as np

img = cv2.imread("temp.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray=cv2.GaussianBlur(img_gray, (7,7),0)
th = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
# ret, th = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY)
kernel = np.ones((7, 7), np.uint8)
dilation = cv2.dilate(th,kernel,iterations = 1)
contours ,_ = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
idx = 0
f = open("output.txt", "a")
for contour in contours:
    area=cv2.contourArea(contour)
    # print(area)
    if area>400 and area<3000:
        idx += 1
        x,y,w,h = cv2.boundingRect(contour) 
        roi = img[y:y+h,x:x+w]
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
        result=x,y,w,h
        f.write(','.join(str(r) for r in result))
        f.write('\n')
        # print(str)
cv2.imshow('output.jpg', img)
cv2.imwrite('output.jpg', img)
cv2.waitKey()