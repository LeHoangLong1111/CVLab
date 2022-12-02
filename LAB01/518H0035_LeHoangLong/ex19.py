##19 Draw a rectangle

import cv2

path = r'lena.png'

img= cv2.imread(path)

start_point = (5,5)

end_point =  (200,200)

color = (255,0,0)

thickness = 5

img = cv2.rectangle(img, start_point, end_point, color, thickness)

cv2.imshow('Result', img)
cv2.imwrite('image_19.jpg',img)
cv2.waitKey(0)