##8 Image Resizing
import cv2
import numpy as np
import matplotlib.pyplot as plt
import putText

img = cv2.imread('pic8.jpg', 1)

half = cv2.resize(img, (0,0), fx=0.1, fy=0.2)
bigger = cv2.resize(img, (1500, 1200))

smaller = cv2.resize(img, (1000, 700),
               interpolation = cv2.INTER_NEAREST)

Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
images =[img, half, bigger, smaller]
count = 4
 
for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])
 
plt.show()