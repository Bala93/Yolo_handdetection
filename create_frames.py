
import sys
import cv2
import numpy as np

# Enter the filename and the number of frames required 
video_file = sys.argv[1]
expected_frames = int(sys.argv[2])
cap = cv2.VideoCapture(video_file)

count = 1
while (cap.isOpened()):

	ret,frame = cap.read()
	imgname = str(count) + '.jpg'
	cv2.imwrite(imgname,frame)

	if count == expected_frames:
		break

	count += 1
	
cap.release()


		
