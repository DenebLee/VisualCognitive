# -*-coding:utf-8
# Show fps on frames
# https://jacegem.github.io/blog/2018/OpenCV-Python-Tutorials-09-%EC%84%B1%EB%8A%A5-%EC%B8%A1%EC%A0%95-%EB%B0%8F-%EA%B0%9C%EC%84%A0-%EA%B8%B0%EB%B2%95/
import cv2
import numpy as np
import time

capture = cv2.VideoCapture(0)
count = 0
fps = 0

# opencv 성능측정에 사용.
t0 = cv2.getTickCount()
time0 = time.time()

while True:
	ret, frame = capture.read()
	# cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) → None
	# - write fps info to video
	cv2.putText(frame, str(fps), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) == 27: break

	count += 1
	if(count == 10):
		t1 = cv2.getTickCount()
		time1 = time.time()
		# delta_time = (t1-t0) / cv2.getTickFrequency()
		delta_time = time1 - time0
		fps = int(np.round(10/delta_time))
		count = 0
		t0 = t1
		time0 = time1

capture.release()