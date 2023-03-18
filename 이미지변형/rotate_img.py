import cv2
src = cv2.imread('img.jpg')

# 시계 방향 90도 회전
rotate_90 = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE) # 시계방향으로 90도 회전

# 180도 회전
rotate_180 = cv2.rotate(src, cv2.ROTATE_180) # 180도 회전

# 시계 반대 방향으로 90도 회전 === 시계 방향 270도 회전
rotate_270 = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE) # 시계방향으로 90도 회전

cv2.imshow('src', src)
cv2.imshow('rotate_90', rotate_90)
cv2.imshow('rotate_180', rotate_180)
cv2.imshow('rotate_270', rotate_270)

cv2.waitKey(0)
cv2.destroyAllWindows()