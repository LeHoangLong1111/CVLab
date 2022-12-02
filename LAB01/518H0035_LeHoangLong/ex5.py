import cv2
import putText
  
image = cv2.imread('lena.png')
putText.putText(image, 'Exercise5')
B, G, R = cv2.split(image)

# Corresponding channels are seperated
  
cv2.imshow("original", image)
cv2.imwrite('image_5(1).jpg',image)
cv2.waitKey(0)
  
cv2.imshow("blue", B)
cv2.imwrite('image_5(2).jpg',B)
cv2.waitKey(0)
  
cv2.imshow("Green", G)
cv2.imwrite('image_5(3).jpg',G)
cv2.waitKey(0)
  
cv2.imshow("red", R)
cv2.imwrite('image_5(4).jpg',R)
cv2.waitKey(0)
  
cv2.destroyAllWindows()