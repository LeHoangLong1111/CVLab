## Draw an ellipse

import cv2

path = r'lena.png'

img= cv2.imread(path)

center_coordinates = (150,150)

axesLength=(50,25)

angle = 0

startAngle = 0

endAngle = 360

color=(255,0,0)

thickness=4

img= cv2.ellipse(img, center_coordinates, axesLength, angle, startAngle, endAngle, color, thickness)

cv2.imshow('Result', img)
cv2.imwrite('image_17.jpg',img)

cv2.waitKey(0)