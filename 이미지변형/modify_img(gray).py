# 이미지 전처리 == 이미지 내에서 관심 없는 부분을 제거하는 과정

import cv2

# 이미지를 흑백으로 "불러옴"
gray = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)

# 불러온 이미지를 "흑백으로 변경"
img = cv2.imread('img.jpg')
dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # opencv 는 bgr로 처리함

cv2.imshow('img', img)
cv2.imshow('gray', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
