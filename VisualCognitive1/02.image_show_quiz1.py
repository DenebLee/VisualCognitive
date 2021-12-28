# [Quiz] 입력된 키보드 값을 문자로 출력하고, ESC인 경우, 프로그램이 종료되도록 한다.
import cv2

img = cv2.imread('image/cat.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('img', img)

while True:
    key = cv2.waitKey(30)
    if key != -1:
        print('key =', key)       # key 값은 ASCII 코드값
        print('key =', chr(key))
    if key == 27:
        break

cv2.destroyAllWindows()