##11 Scaling, Rotating, Shifting and Edge Detection

import cv2
import numpy as np

FILE_NAME = 'lena.png'

#scaling
try:
    img = cv2.imread(FILE_NAME)

    (height, width) = img.shape[:2]

    res = cv2.resize(img, (int(width/2), int(height/2)), interpolation=cv2.INTER_CUBIC)

    cv2.imwrite('image_11(1).jpg',res)

except IOError:
    print('Error Scalling')

#Rolating:
try:
    (rows, cols) = img.shape[:2]

    Matrix = cv2.getRotationMatrix2D((cols/2, rows/2),45,1)
    res1=cv2.warpAffine(img, Matrix, (cols, rows))

    cv2.imwrite('image_11(2).jpg',res1)
except IOError:
    print('Error Rolating')

##Translating:

Matrix2= np.float32([[1,0,70],[0,1,20]])

try:
    (rows, cols) = img.shape[:2]

    res2=cv2.warpAffine(img, Matrix, (cols, rows))

    cv2.imwrite('image_11(3).jpg',res2)

except IOError:
    print('Error Translating')

##Edge Detection
try:

    edges = cv2.Canny(img,100,200)
    cv2.imwrite('image_11(3).jpg',edges)

except IOError:
    print('Error Edge')



