## Draw a line

import cv2

path = r'lena.png'

img= cv2.imread(path)

start = (0,0)

end = (250,250)

color=(0,0,255)

thickness=8

img= cv2.line(img, start, end, color, thickness)

cv2.imshow('Result', img)
cv2.imwrite('image_15.jpg',img)
cv2.waitKey(0)