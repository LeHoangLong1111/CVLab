import cv2

def putText(image, abc):
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # org
    org = (50, 50)
    
    # fontScale
    fontScale = 1
    
    # Blue color in BGR
    color = (255, 155, 0)
    
    # Line thickness of 2 px
    thickness = 2
    
    # Using cv2.putText() method
    image = cv2.putText(image, abc , org, font, 
                    fontScale, color, thickness, cv2.LINE_AA)

    return image