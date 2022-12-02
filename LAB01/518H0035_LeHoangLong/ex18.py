## Draw a circle

import cv2

path = r'lena.png'

img= cv2.imread(path)

center_coordinates = (120,150)

radius = 30

color = (255,255,0)

thickness=-1

img = cv2.circle(img, center_coordinates, radius, color, thickness)

cv2.imshow('Result', img)
cv2.imwrite('image_18.jpg',img)
cv2.waitKey(0)