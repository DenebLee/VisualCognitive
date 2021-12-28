# [Quiz] 3에서 TM_CCOEFF_NORMED를 사용할 때의 결과를 출력해보자. maxValue를 선택해야 한다.
import cv2
import numpy as np
from scipy import ndimage
# TARGET = "image/hats_smallDim.png"
TARGET = "image/hats_smallDimInverse.png"

# 1. View original image
src = cv2.imread(TARGET)
templit = cv2.imread("image/hat.png")

cv2.imshow("hats", src)
cv2.imshow("hst", templit)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. open image for templete matching
src = cv2.imread(TARGET, cv2.IMREAD_GRAYSCALE)
templit = cv2.imread("image/hat.png", cv2.IMREAD_GRAYSCALE)

# - for output of templete matching
dst = cv2.imread(TARGET)

# 3. search templete image
# cv2.matchTemplate(img, template, method)
# - method: 탐색방법
# --- TM_SQDIFF, TM_SQDIFF_NORMED는 최소값이 유사, 그 이외는 최대값이 유사
# --- TM_CCORR, TM_CCORR_NORMED : 상관관계를 이용한 유사도
# --- TM_CCOEFF, TM_CCOEFF_NORMED : 상관계수를 이용한 유사도
# --- result.shape = (W-w+1, H-h+1) : template 필터 공간에서의 유사도값

# --- templit의 크기를 줄여가며 matching한다.
print("src shape : ", src.shape)
best = {}
maxLocs, maxVals, tmpl_hws, resizes, rots = [], [], [], [], []
MAXVAL = 0

# 회전시키는 중에, templit 이미지가 커지면, matchTemplate 에러 발생
resizeFactors = [round(j*0.1, 1) for j in range(6, 0, -1)]

# 이제 이미지를 회전하는 것 까지 적용하자
for rs in resizeFactors:
    print(f"templit is resized with {int(rs*100)} %")
    resized = cv2.resize(templit, dsize=(0, 0), fx=rs, fy=rs, interpolation=cv2.INTER_AREA)

    for rot in range(0, 360, 15):
        print(f"templit is ratated with {rot} angle")
        rotated = ndimage.rotate(resized, rot, cval=255)
        print("rotated.shape : ", rotated.shape)
        res = cv2.matchTemplate(src, rotated, cv2.TM_CCOEFF_NORMED)
        # print("templit shape : ", rotated.shape)
        # print("result shape : ", res.shape)

        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)
        maxVals.append(maxVal)
        maxLocs.append(maxLoc)
        resizes.append(rs)
        rots.append(rot)
        tmpl_hws.append(rotated.shape[:2])

        x, y = maxLoc
        h, w = rotated.shape
        # cv2.rectangle(dst, (x, y), (x + w, y + h), (255, 0, 0), 1)
        # cv2.putText(dst, str(rs), (x, max(y-4, 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)

        if maxVal > MAXVAL:
            print(f"In now, best max value is {maxVal} at {int(rs*100)}% resized and {rot} rotated templit")
            best['maxVal'] = maxVal
            best['maxLoc'] = maxLoc
            best['hw'] = rotated.shape[:2]
            best['result'] = res
            best['resizeRate'] = rs
            best['rotation'] = rot
            MAXVAL = maxVal

# top 10 matching box drowing
top10Idx = np.argsort(maxVals)[-10:]
for i in top10Idx:
    x, y = maxLocs[i]
    h, w = tmpl_hws[i]
    rs = resizes[i]
    rot = round(rots[i], 2)
    maxV = round(maxVals[i], 3)
    title = f"maxnVal {maxV} at {rs} resized, {rot} rotated image"
    cv2.rectangle(dst, (x,y), (x+w, y+h) , (255,0,0), 1)
    cv2.putText(dst, title, (x, max(y-4, 4)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,0,0), 1)


# print(best)
x, y = best['maxLoc']
h, w = best['hw']

# best 매칭 이미지 localization
dst = cv2.rectangle(dst, (x, y), (x + w, y + h) , (0, 0, 255), 3)
cv2.putText(dst, str(best['resizeRate']), (x, max(y-4, 4)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

cv2.imshow("rst", best['result'])
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()