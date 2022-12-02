import cv2

##1 Sobel
img = cv2.imread('input1.jpg',flags=0) 
img_blur = cv2.GaussianBlur(img,(3,3), sigmaX=0, sigmaY=0)


sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection

# cv2.imshow('Sobel X', sobelx) # Display Sobel Edge Detection Images
# cv2.waitKey(0)
cv2.imwrite('sobelX.jpg', sobelx) 
# cv2.imshow('Sobel Y', sobely)
# cv2.waitKey(0)
cv2.imwrite('sobelY.jpg', sobely) 
# cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
# cv2.waitKey(0)
cv2.imwrite('sobelXY.jpg', sobelxy)


##Canny
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
# cv2.imshow('Canny Edge Detection', edges)
# cv2.waitKey(0)
cv2.imwrite('canny.jpg', edges)


## Hough Line
import sys
import math
import cv2 as cv
import numpy as np
def houghLine(argv):
    default_file = 'sudoku.jpg'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_GRAYSCALE)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_lines.py [image_name -- default ' + default_file + '] \n')
        return -1
    
    dst = cv.Canny(src, 50, 200, None, 3)
    
    # Copy edges to the images that will display the results in BGR
    cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)
    lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)
    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv.line(cdst, pt1, pt2, (100,200,255), 3, cv.LINE_AA)
    
    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
    
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (100,200,255), 3, cv.LINE_AA)
    
    # cv.imshow("Source", src)
    # cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
    cv2.imwrite('StandardHoughLine.jpg', cdst)
    # cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)
    cv2.imwrite('ProbabilisticLine.jpg', cdstP)
    cv.waitKey()
    return 0
    
houghLine(sys.argv[1:])

## Hough Circle

def houghCircle(argv):
    default_file = 'hough_circles_demo_01.png'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1
    
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    
    gray = cv.medianBlur(gray, 5)
    
    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,  param1=100, param2=30,minRadius=1, maxRadius=30)
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            cv.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv.circle(src, center, radius, (100,200,255), 3)
    
    # cv.imshow("detected circles", src)
    # cv.waitKey(0)
    cv2.imwrite("detectedCircle.png", src)
    return 0

houghCircle(sys.argv[1:])

