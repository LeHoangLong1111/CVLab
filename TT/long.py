import cv2

def get_value(pos):
    get_value.value=pos
get_value.value = 0

cv2.namedWindow("Control")
cv2.createTrackbar("Value", "Control", 0, 255, get_value)

while True:
    img = cv2.imread('sudoku-original.jpg',0)
    cv2.imshow("Control",img)

    ret,re = cv2.threshold(img, get_value.value,255, cv2.THRESH_BINARY )
    # print(ret)
    # re = cv2.adaptiveThreshold(img, get_value.value, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,3,0)
    cv2.imshow("Result", re)

    if cv2.waitKey(10) == ord('q'):
        break
cv2.destroyAllWindows()
