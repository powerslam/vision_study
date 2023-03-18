import cv2
src = cv2.imread('img.jpg')
cv2.imshow('src', src)

# 1. 좌우 대칭 : flipCode > 0
flip_horizontal = cv2.flip(src, 1)
#                         원본, flipCode
cv2.imshow('flip_horizontal', flip_horizontal)

# 2. 상하 대칭 : flipCode == 0
flip_vertical = cv2.flip(src, 0)
cv2.imshow('flip_vertical', flip_vertical)

# 3. 원점 대칭 : flipCode < 0
flip_both = cv2.flip(src, -1)
cv2.imshow('flip_both', flip_both)

cv2.waitKey(0)
cv2.destroyAllWindows()
