# [Quiz] googloLogo.png 파일의 파탕을 검정색으로 변환하고,
# 구글 로고의 size를 절반으로 줄여서, bit_test.jpb 파일의 가운데에 위치시키자.

import cv2
import numpy as np

img = cv2.imread('bit_test.jpg', cv2.IMREAD_COLOR)
google = cv2.imread('googleLogo.png', cv2.IMREAD_COLOR)
# cv2.resize(src, dsize, fx, fy, interpolation)
logo = cv2.resize(google, dsize=(0,0), fx=.5, fy=.5)

logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
# logo_gray = np.where(logo_gray == 255, 0, logo_gray)
logo_gray = np.where(logo_gray > 200, 0, logo_gray)
_, mask = cv2.threshold(logo_gray, 10, 255, cv2.THRESH_BINARY)

rows, cols = img.shape[:2]
logo_rows, logo_cols = logo.shape[:2]
starty, startx = (rows - logo_rows) // 2, (cols - logo_cols) // 2

roi = img[starty:starty+logo_rows, startx:startx+logo_cols]

roi[mask.astype(bool)] = logo[mask.astype(bool)]
# equivalent with cv2.copyTo(src, mask, dst)
# cv2.copyTo(logo, mask, roi)

cv2.imshow('res', img)
# cv2.imshow('google', logo)
cv2.waitKey(0)
cv2.destroyAllWindows()