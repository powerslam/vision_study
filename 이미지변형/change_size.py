# 동영상에서도 방법은 똑같다.
# frame에 다음 방법들을 적용하여 사이즈를 바꿀 수 있다.

import cv2
img = cv2.imread('img.jpg')

# 크기 조정
# 1. 고정 크기로 설정
fixed_dst = cv2.resize(img, (400, 500)) # width, height 고정 크기

cv2.imshow('img', img)
cv2.imshow('resize', fixed_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. 비율로 설정
# 비율이기 때문에 크기부분에는 None을 넘김
ratio_dst = cv2.resize(img, None, fx=0.5, fy=0.5) # x, y 비율 정의 (0.5 배로 축소)

cv2.imshow('img', img)
cv2.imshow('resize', ratio_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 보간법
# 크기가 변경될 때 생기는 빈 공간을 자연스럽게 줄이기 위한 방법론

# 1. cv2.INNER_AREA = 크기 줄일 때 사용
# 2. cv2.INTER_CUBIC = 크기 늘릴 때 사용 (속도 느림, 퀄리티 좋음)
# 3. cv2.INTER_LINEAR = 크기 늘릴 때 사용 (기본값)

inner_area_dst = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA) 
inter_cubic_dst = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC) 
inter_linear = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR) 

cv2.imshow('img', img)
cv2.imshow('inner_area', inner_area_dst)
cv2.imshow('inter_cubic', inter_cubic_dst)
cv2.imshow('inter_linear', inter_linear)
cv2.waitKey(0)
cv2.destroyAllWindows()
