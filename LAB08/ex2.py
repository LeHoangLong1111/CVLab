import os
import re
import cv2
import numpy as np
# from tqdm.notebook import tqdm
from tqdm import tqdm, notebook
import matplotlib.pyplot as plt
import glob
from os.path import isfile, join

col_frames = os.listdir('frames/')
col_frames.sort(key=lambda f: int(re.sub('\D', '', f)))

# load frames
col_images = []
for i in tqdm(col_frames):
    img = cv2.imread('frames/'+i)
    col_images.append(img)

# specify frame index
idx = 457

# plot frame
plt.figure(figsize=(10, 10))
plt.imshow(col_images[idx][:, :, 0], cmap="gray")
plt.show()

# create a zero array
stencil = np.zeros_like(col_images[idx][:, :, 0])

# specify coordinates of the polygon
polygon = np.array([[50, 270], [220, 160], [360, 160], [480, 270]])

cv2.fillConvexPoly(stencil, polygon, 1)
ret, thresh = cv2.threshold(img, 130, 145, cv2.THRESH_BINARY)

# draw Hough lines
cnt = 0

for img in tqdm(col_images):
    # apply frame mask
    masked = cv2.bitwise_and(img[:, :, 0], img[:, :, 0], mask=stencil)
    # apply image thresholding
    ret, thresh = cv2.threshold(masked, 130, 145, cv2.THRESH_BINARY)
    # apply Hough Line Transformation
    lines = cv2.HoughLinesP(thresh, 1, np.pi/180, 30, maxLineGap=200)
    dmy = img.copy()
    # Plot detected lines
    try:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(dmy, (x1, y1), (x2, y2), (255, 0, 0), 3)
        cv2.imwrite('frames/'+str(cnt)+'.png', dmy)
    except TypeError:
        cv2.imwrite('frames/'+str(cnt)+'.png', img)
    cnt += 1

pathIn = 'frames/'

# specify frames per second
fps = 30.0
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
files.sort(key=lambda f: int(re.sub('\D', '', f)))

frame_list = []

for i in tqdm(range(len(files))):
    filename = pathIn + files[i]
    # reading each files
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    frame_list.append(img)

img_array = []
for filename in glob.glob('frames/*.png'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
out = cv2.VideoWriter('result.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()