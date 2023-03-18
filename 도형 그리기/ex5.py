import cv2
import numpy as np
img = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (255, 255, 0)
RADIUS = 50
THICKNESS = 3

cv2.circle(img, (200, 100), RADIUS, COLOR, THICKNESS, cv2.LINE_AA)

# THICKNESS 대신에 cv2.FILLED를 넣으면 꽉 채워진다.
cv2.circle(img, (400, 100), RADIUS, COLOR, cv2.FILLED, cv2.LINE_AA)

COLOR = (0, 255, 0)

# 정사각형이기 때문에 라인 타입을 정할 필요는 없다
cv2.rectangle(img, (150, 200), (250, 300), COLOR, THICKNESS)

# THICKNESS 대신에 cv2.FILLED를 넣으면 꽉 채워진다.
cv2.rectangle(img, (350, 200), (450, 300), COLOR, cv2.FILLED)


cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
