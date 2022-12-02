import cv2
import numpy as np

video = cv2.VideoCapture(0)

image_logo = cv2.imread('logo.png')


width = 150
height = 80

image_logo = cv2.resize(image_logo, (width, height))
  
ret, mask = cv2.threshold(image_logo, 0, 255, cv2.THRESH_BINARY)
  
while True:
    ret, frame = video.read()
    index = frame[-height-5:-5, -width-5:-5]
    index[np.where(mask)] = 0
    index += image_logo
  
    cv2.imshow('WebCam', frame)

    if cv2.waitKey(1) == ord('c'):
        break

video.release()
cv2.destroyAllWindows()
