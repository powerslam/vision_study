import cv2
import numpy as np

img1 = cv2.imread('newspaper.jpg')

w, h = 640, 240
# 왼쪽 위부터 시계방향으로 점을 찾음
# input pts
src = np.array([[511, 350], [1008, 345], [1122, 584], [455, 594]], dtype=np.float32)

# output pts
dst = np.array([[0, 0], [w, 0], [w, h], [0, h]], dtype=np.float32)

# 좌상, 우상, 우하, 좌하 (시계 방향으로 4 지점 정의)

matrix = cv2.getPerspectiveTransform(src, dst) # src -> dst 를 위한 matrix를 계산함
result1 = cv2.warpPerspective(img1, matrix, (w, h)) # matrix 대로 변환을 함

cv2.imshow('img1', img1)
cv2.imshow('result1', result1)

img2 = cv2.imread('poker.jpg')
w, h = 530, 710
# input pts
src = np.array([[702, 143], [1133, 414], [726, 1007], [276, 700]], dtype=np.float32)

# output pts
dst = np.array([[0, 0], [w, 0], [w, h], [0, h]], dtype=np.float32)

matrix = cv2.getPerspectiveTransform(src, dst) # src -> dst 를 위한 matrix를 계산함
result2 = cv2.warpPerspective(img2, matrix, (w, h)) # matrix 대로 변환을 함

cv2.imshow('img2', img2)
cv2.imshow('result2', result2)

cv2.waitKey(0)
cv2.destroyAllWindows()
