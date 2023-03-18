# 흐림 = blur = 보이는 정보를 조정해서 외곽선 따는 작업을 쉽게 만듬
import cv2
src = cv2.imread('img.jpg')

# 대표적으로 가우시안 블러가 있음
# 1. 커널 사이즈(2번째 인자) 변화에 따른 흐림
kernel_3 = cv2.GaussianBlur(src, (3, 3), 0)
kernel_5 = cv2.GaussianBlur(src, (5, 5), 0)
kernel_7 = cv2.GaussianBlur(src, (7, 7), 0)

cv2.imshow('img', src)
cv2.imshow('kernel_3', kernel_3)
cv2.imshow('kernel_5', kernel_5)
cv2.imshow('kernel_7', kernel_7)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. 표준 편차(3번째 인자) 변화에 따른 흐림 = 커널 사이즈가 (0, 0)일 때
sigma_1 = cv2.GaussianBlur(src, (0, 0), 1)
sigma_2 = cv2.GaussianBlur(src, (0, 0), 2)
sigma_3 = cv2.GaussianBlur(src, (0, 0), 3)

cv2.imshow('img', src)
cv2.imshow('sigma_1', sigma_1)
cv2.imshow('sigma_2', sigma_2)
cv2.imshow('sigma_3', sigma_3)

# 1번에서도 표준편차를 키우면 블러효과가 진해진다.

cv2.waitKey(0)
cv2.destroyAllWindows()
