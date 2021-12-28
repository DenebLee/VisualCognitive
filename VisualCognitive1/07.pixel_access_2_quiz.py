# [Quiz]
# 1. cat이미지의 명도를 1/2로 줄인 half 이미지와
# 2. cat이미지의 명도를 2배로 늘린 twice 이미지를 생성하세요.

import cv2
import numpy as np

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)
half = img // 2
cv2.imshow('half', half)

twice = np.where(img > 127, 255, img*2)
cv2.imshow('twice', twice)

# 잘 못된 예 - overflow 발생
twice2 = img*2
cv2.imshow('twice2', twice2)

cv2.waitKey()

