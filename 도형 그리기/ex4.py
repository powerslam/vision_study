import cv2
import numpy as np
# cv2 는 BGR로 처리한다

# 세로 480, 가로 640, 채널 3 인 이미지
# 데이터 타입은 np.uint8
img = np.zeros((480, 640, 3), dtype=np.uint8)
# np.zeros(shape, dtype) == dtype과 shape 에 맞게 0으로 채워진 배열을 준다
# img[:] = (255, 255, 255) # 전체 공간을 흰색으로 채우기

# 높이 : 100 ~ 200 / 너비 : 200 ~ 300 영역을 흰색으로 바꾸는 코드
img[100:200, 200:300] = (255, 255, 255)

# 직선의 종류
# 1. cv2.LINE_4 : 상하좌우 4 방향으로 연결된 선
# 2. cv2.LINE_8 : 대각 포함 상하좌우 8 방향으로 연결된 선 (기본값)
# 3. cv2.LINE_AA : 부드러운 선 (anti-aliasing)

COLOR = (0, 255, 255) # BGR : Yellow
THICKNESS = 3 # 두께

# image, p1, p2, 색, 두께, 선의 종류
cv2.line(img, (50, 70), (400, 20), COLOR, THICKNESS, cv2.LINE_4)
cv2.line(img, (50, 100), (400, 50), COLOR, THICKNESS, cv2.LINE_8)
cv2.line(img, (50, 130), (400, 80), COLOR, THICKNESS, cv2.LINE_AA)

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
