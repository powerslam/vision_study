import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (0, 0, 255)
THICKNESS = 3

pts1 = np.array([[100, 100], [200, 100], [100, 200]])
pts2 = np.array([[200, 100], [300, 100], [300, 200]])

# pts : [] 안에 원하는 꼭짓점의 집합을 넣는 것
#       ex) [pts1, pts2] : pts1 도형, pts2 도형 모두 그려짐 

# isClosed : True  -> pts1의 모든 점들 끼리 연결됨 
#            False -> pts1의 시작점, 끝점만 연결이 안 됨
cv2.polylines(img, [pts1], False, COLOR, THICKNESS, cv2.LINE_AA)
cv2.polylines(img, [pts2], True, COLOR, THICKNESS, cv2.LINE_AA)
# 배경, 위치들 ([점들, 점들, 점들]), isClosed, Color, THICKNESS, 선 모양

pts3 = np.array([[[100, 300], [200, 300], [100, 400]], [[200, 300], [300, 300], [300, 400]]])
# 꽉찬 다각형
# 배경, 위치들, 색깔, 선 모양
cv2.fillPoly(img, pts3, COLOR, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

