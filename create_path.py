import sys
import glob


arg = (sys.argv)
train_path = arg[1]
test_path  = arg[2]

# This is to get the image files in the format which is expected in yolo

with open('train.txt','w') as f:
	tp = train_path + '*.jpg'
	print tp
	for i in glob.glob(tp):
		
		f.write(i+'\n')


with open('test.txt','w') as f:
	tp = test_path + '*.jpg'
	print tp
	for i in glob.glob(tp):
		
		f.write(i+'\n')


