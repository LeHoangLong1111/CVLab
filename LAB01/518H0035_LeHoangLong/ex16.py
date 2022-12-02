## Draw arrow segment

import cv2

path = r'lena.png'

img= cv2.imread(path)

start = (0,0)

end = (100,200)

color=(255,0,0)

thickness=8

img= cv2.arrowedLine(img, start, end, color, thickness, tipLength=0.5)

cv2.imshow('Result', img)
cv2.imwrite('image_16.jpg',img)
cv2.waitKey(0)