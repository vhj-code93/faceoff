# Importing all necessary libraries 
import cv2 
import os 

# Read the video from specified path 
# specify name of the video you recorded
cam = cv2.VideoCapture("touch.mov") 

try: 
	
	# creating a folder named data 
	if not os.path.exists('touch-data'): 
		os.makedirs('touch-data') 

# if not created then raise error 
except OSError: 
	print ('Error: Creating directory of touch-data') 

# frame 
currentframe = 0

while(True): 
	
	# reading from frame 
	ret,frame = cam.read() 

	if ret: 
		# if video is still left continue creating images 
		# use the right naming convention
		name = './touch-data/frame' + str(currentframe) + '.jpg'
		print ('Creating...' + name) 

		# writing the extracted images 
		cv2.imwrite(name, frame) 

		# increasing counter so that it will 
		# show how many frames are created 
		currentframe += 1
	else: 
		break

# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 
