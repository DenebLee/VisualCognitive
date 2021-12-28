# set all red channels to 0

import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow('org', img)

img[:,:,2] = 0

cv2.imshow('cvt',img)
cv2.waitKey()