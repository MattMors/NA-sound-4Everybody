import cv2
import os

# we can use object recognition to recognize stars in the video and generate sound when detected
# THIS PROJECT IS AN ALPHA AND DOESN'T USE THIS FEATURE

#Const
frame_dir = 'videos/frames'
video = 'C:\\Users\\matte\\Desktop\\Hackaton_nasa\\code\\videos\\cosmic_reef.mp4' #cosmic_reef.mp4' #space_video_1

cap = cv2.VideoCapture(video)

if (cap.isOpened() == False):
    print("Error opening video file")


object_detector = cv2.createBackgroundSubtractorMOG2(history=40, varThreshold=200)

frame_obj_dict = {}

frame_count = -1

timestamp = 0

while True:

	frame_count += 1

	cap.set(cv2.CAP_PROP_POS_MSEC, timestamp)

	ret, frame = cap.read()

	if frame is None:
		break

	#region of interest
	roi = frame[:,680:880] # height 720,width 1280



	mask = object_detector.apply(roi)
	_ , mask = cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
	contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	n_obj = 0

	for cnt in contours:

		#calculate area and remove small elements
		area = cv2.contourArea(cnt)

		if area > 80 and area < 2000:

			startX, startY, w, h = cv2.boundingRect(cnt)
			endX = startX + w
			endY = startY + h

			#cv2.rectangle(roi, (startX, startY), (endX, endY), (150, 0, 120), 3)

			n_obj +=1

	frame_obj_dict.update({frame_count:n_obj})

	# cv2.imshow("Frame",frame)
	#interrupt key
	#key = cv2.waitKey(30)
	#if key == 1:
	#	break

	timestamp += 1000

print(frame_obj_dict.keys())
print(frame_obj_dict.values())

cap.release()
cv2.destroyAllWindows()
