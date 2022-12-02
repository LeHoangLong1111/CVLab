##1. Split each color channel of the image
import numpy as np
import cv2
import putText

image = cv2. imread('ballon.PNG')

b ,g ,r = cv2.split(image)

img1 = cv2.merge((b,g,r))

cv2.imshow("Blue",b)
cv2.waitKey(0)
cv2.imshow("Green",g)
cv2.waitKey(0)
cv2.imshow("Red",r)
cv2.waitKey(0)
cv2.imshow("Result",img1)
cv2.imwrite('image_1_1.PNG', img1)
cv2.waitKey(0)

##2 Locate the position of each balloon by drawing a rectangle (bounding-box) surrounding each balloon

image = cv2. imread('ballon.PNG')

## Yellow

start_point = (21,40)
end_point = (195,595)

color = (0, 255, 255)

thickness = 2

image_yellow = cv2.rectangle(image, start_point, end_point, color, thickness)

# cv2.imshow('Image Yellow', image_yellow)
# cv2.waitKey(0)

## blue
start_point = (215,121)
end_point = (358,615)

color = (255, 0, 0)

thickness = 2

image_blue = cv2.rectangle(image, start_point, end_point, color, thickness)

# cv2.imshow('Image blue', image_blue)
# cv2.waitKey(0)

## red
start_point = (381,53)
end_point = (559,619)

color = (0, 0, 255)

thickness = 2

image_red = cv2.rectangle(image, start_point, end_point, color, thickness)

# cv2.imshow('Image red', image_red)
# cv2.waitKey(0)

##green
start_point = (584,115)
end_point = (762,619)

color = (0, 255, 0)

thickness = 2

image_green = cv2.rectangle(image, start_point, end_point, color, thickness)

# cv2.imshow('Image green', image_green)
# cv2.waitKey(0)

##orange
start_point = (774,50)
end_point = (946,622)

color = (0, 165, 255)

thickness = 2

image_orange = cv2.rectangle(image, start_point, end_point, color, thickness)

# cv2.imshow('Image orange', image_orange)
# cv2.waitKey(0)
cv2.imwrite('image_1_2.PNG', image_orange)

##3 Name each balloon by putting a text of color name right above the bounding boxes.

##Yellow
org_yellow = (78,23)
putText.putText(image_orange, 'Yellow', org_yellow, (0, 255, 255))

# cv2.imshow('Result Yellow Text', image_orange)
# cv2.waitKey(0)

## blue
org_blue = (260,97)
putText.putText(image_orange, 'Blue', org_blue, (255, 0, 0))
# cv2.imshow('Result Blue Text', image_orange)
# cv2.waitKey(0)

##red
org_red = (437,32)
putText.putText(image_orange, 'Red', org_red, (0, 0, 255))

##green
org_green = (620,95)
putText.putText(image_orange, 'Green', org_green, (0, 255, 0))

##orange
org_orange = (820,28)
putText.putText(image_orange, 'Orange', org_orange, (0, 165, 255))
cv2.imshow('Result Text', image_orange)
cv2.imwrite('image_1_3.PNG', image_orange)
cv2.waitKey(0)

## 4 Extract the yellow balloon by creating a new image of only one balloon.
image = cv2. imread('ballon.PNG')
ballon_yellow = image[ 36:612, 20:200]
# cv2.imshow('Ballon_yellow', ballon_yellow)
# cv2.waitKey(0)
cv2.imwrite('image_1_4.PNG', ballon_yellow)

##5 Extract the yellow balloon automatically by using HSV color space to extract only pixels of yellow color.

image = cv2. imread('ballon.PNG')
imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_h=np.array([20,100,100])
higher_h = np.array([30,255,255])
mask = cv2.inRange(imageHSV, lower_h, higher_h)
cv2.imwrite('image_1_5.PNG', mask)
cv2.imshow('Image_5',mask)
cv2.waitKey(0)

##6 Re-paint the yellow balloon by replacing the pixels of yellow by green.
image = cv2. imread('ballon.PNG')
(h,w) = image.shape[:2]
# print(image.shape)
# print('h: ', h)
# print('w: ',w)
pw=w//5

green_ballon = image[0:h, pw*3:pw*4]
image[0:h, 15:pw+15] = green_ballon
cv2.imshow("image_1.6",image)
cv2.imwrite('image_1_6.PNG', image)
cv2.waitKey(0)

##7 Rotate the first balloon an angle of 20 degree
image = cv2. imread('ballon.PNG')
(h,w) = image.shape[:2]
pw=w//5
first_ballon = image[0:h,0:pw+15]
(dx, dy)=(w//2, h//2)
R=cv2.getRotationMatrix2D((dx,dy), 20, 1)
res=cv2.warpAffine(first_ballon, R,(h,w))
cv2.imshow("first_ballon", res)
cv2.imwrite('image_1_7.PNG', res)
cv2.waitKey(0)







