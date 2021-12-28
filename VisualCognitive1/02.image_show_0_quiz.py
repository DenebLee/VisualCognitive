# [Quiz] image 폴더에 있는 min_max.jpg 파일을
# 1. 흑백영상으로 읽고
# 2. 그 shape을 출력하고
# 3. 그 이미지를 IMG 창에 출력한다.
# 4. 이미지에서 20 ~ 40 색인의 height와 width 값을 0으로 변경한 배열을 img2로 하고
# 5. img2 배열을 IMG2 창에 출력한다.

import cv2
import numpy as np

img = cv2.imread('image/min_max.jpg', cv2.IMREAD_GRAYSCALE)

# create window with WINDOW_AUTOSIZE
cv2.imshow('IMG', img)
print(img.shape)

img2 = img.copy()
img2[20:40, 20:40] = 0
cv2.imshow('IMG2', img2)
cv2.waitKey(0)

# all windows is closed
cv2.destroyAllWindows()

# [Quiz] MASK 영역을 파란색 또는 빨간색 또는 노란색으로 변경하자.

# MASK = np.array([0,255,255])
#
# img = cv2.imread('image/min_max.jpg')
#
# # create window with WINDOW_AUTOSIZE
# cv2.imshow('IMG', img)
# print(img.shape)
#
# img2 = img.copy()
# img2[20:40, 20:40, :] = MASK
# cv2.imshow('IMG2', img2)
# cv2.waitKey(0)
#
# # all windows is closed
# cv2.destroyAllWindows()
#
# # [Quiz] MASK 영역을 파란색 또는 빨간색 또는 노란색으로 변경하자.