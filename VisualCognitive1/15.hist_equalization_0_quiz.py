# [Quiz] RGB 색상별로 bin 64의 히스토그램을 그리고, 원본과 평활화이미지를 비교해보자.

import cv2
from matplotlib import pyplot as plt

img0 = cv2.imread('cat.jpg')

# BGR 컬러공간으로 변환후 각 채널별 평평히
b, g, r = cv2.split(img0)
b1 = cv2.equalizeHist(b)
g1 = cv2.equalizeHist(g)
r1 = cv2.equalizeHist(r)
img_eqal = cv2.merge((b1,g1,r1)) #각 채널별 평평해진 이미지

# HSV 컬러공간으로 변환후 명도 Value 채널만 평평히
hsv = cv2.cvtColor(img0, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
# h1 = cv2.equalizeHist(h)
# s1 = cv2.equalizeHist(s)
v1 = cv2.equalizeHist(v)
# hsv1 = cv2.merge((h1,s1,v1))
hsv1 = cv2.merge((h,s,v1)) #평평해진 Value 채널로 대체
img_hsv = cv2.cvtColor(hsv1, cv2.COLOR_HSV2BGR)

# YCrCb 컬러공간으로 변환후 명도 Y 채널만 평평히
YCrCb = cv2.cvtColor(img0, cv2.COLOR_BGR2YCrCb)
y, r, b = cv2.split(YCrCb)
y1 = cv2.equalizeHist(y)
Y1CrCb = cv2.merge((y1,r,b)) #평평해진 Y 채널로 대체
img_YCrCb = cv2.cvtColor(Y1CrCb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('img0', img0)
cv2.imshow('img_rgb', img_eqal)
cv2.imshow('img_hsv', img_hsv)
cv2.imshow('img_YCrCb', img_YCrCb)
cv2.waitKey()

color = ['b', 'g', 'r']

fig, axes = plt.subplots(1,4, sharex=True, sharey=True, figsize=(20,5))
# 원본 img에 대해 루프를 세번 돌며 각각의 컬러별로 히스토그램 계산
for i, c in enumerate(color):
	hist = cv2.calcHist([img0], [i], None, [64], [0,256])
	axes[0].plot(hist, color=c)
	axes[0].set_xlim([0,64])
	axes[0].set_ylim([0,12000])
	axes[0].set_title("original")

# bgr eqaulized img에 대해 루프를 세번 돌며 각각의 컬러별로 히스토그램 계산
for i, c in enumerate(color):
	hist = cv2.calcHist([img_eqal], [i], None, [64], [0,256])
	axes[1].plot(hist, color=c)
	axes[1].set_xlim([0,64])
	axes[1].set_ylim([0,12000])
	axes[1].set_title("RGB_equalized")

# 루프를 세번 돌며 각각의 컬러별로 히스토그램 계산
for i, c in enumerate(color):
	hist = cv2.calcHist([img_hsv], [i], None, [64], [0,256])
	axes[2].plot(hist, color=c)
	axes[2].set_xlim([0,64])
	axes[2].set_ylim([0,12000])
	axes[2].set_title("HSVEqualized")

# 루프를 세번 돌며 각각의 컬러별로 히스토그램 계산
for i, c in enumerate(color):
	hist = cv2.calcHist([img_YCrCb], [i], None, [64], [0,256])
	axes[3].plot(hist, color=c)
	axes[3].set_xlim([0,64])
	axes[3].set_ylim([0,12000])
	axes[3].set_title("YCrCbEqualized")

plt.show()
cv2.destroyAllWindows()