import numpy as np
import cv2


cap = cv2.VideoCapture('demo.mp4')
frameIds = cap.get( v2.CAP_PROP_FRAME_COUNT)*np.random.uniform(size=25)
caps = []
for fid in frameIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = cap.read()
    caps.append(frame)
medianCap = np.median(caps, axis=0).astype(dtype=np.uint8)    
cv2.imshow('cap', medianCap)


cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
grayMedianFrame = cv2.cvtColor(medianCap, cv2.COLOR_BGR2GRAY)
ret = True
while(ret):
  # Read frame
  ret, frame = cap.read()
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # Calculate absolute difference of current frame and 
  dframe = cv2.absdiff(frame, grayMedianFrame)
  # Treshold to binarize
  th, dframe = cv2.threshold(dframe, 40, 255, cv2.THRESH_BINARY)
  cv2.imshow('video', dframe)
  cv2.waitKey(20)

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()