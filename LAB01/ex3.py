##3 Writing an image in OpenCV using Python
import cv2
import os
import putText

path='lena.png'
directory = r'./'


image = cv2.imread(path)
putText.putText(image, 'Exercise3')


# Change the current directory 
# to specified directory 
os.chdir(directory)

# List files and directories  
# in ''
print('Before saving image: ')
print(os.listdir(directory))

#Filename
filename="image_3.jpg"

# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, image)

# List files and directories  
# in r'./'
print("After saving image:")  
print(os.listdir(directory)) 

print('Successfully saved')