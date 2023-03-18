# OpenCV에서 사용하는 글꼴
# 1. cv2.FONT_HERSHEY_SIMPLEX : 보통 크기의 산 세리프 글꼴
# 2. cv2.FONT_HERSHEY_PLAIN   : 작은 크기의 산 세리프 글꼴
# 3. cv2.FONT_HERSHEY_SCRIPT_SIMPLEX : 필기체 스타일 글꼴
# 4. cv2.FONT_HERSHEY_TRIPLEX: 보통 크기의 굵은 산 세리프 글꼴

# 5. cv2.FONT_ITALIC : 기울임 (이탤릭체) ==> 다른 글꼴이랑 같이 써야 함

import numpy as np
import cv2

img = np.zeros((480, 640, 3), dtype=np.uint8)

SCALE = 2
COLOR = (255, 255, 255)
THICKNESS = 3

# 배경, 텍스트 내용, 시작 위치, 폰트 종류, 크기, 색깔, 두께
cv2.putText(img, "Nado Simplex", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, "Nado Simplex", (20, 150), cv2.FONT_HERSHEY_PLAIN, SCALE, COLOR, THICKNESS)
cv2.putText(img, "Nado Simplex", (20, 250), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, "Nado Simplex", (20, 350), cv2.FONT_HERSHEY_TRIPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, "Nado Simplex", (20, 450), cv2.FONT_HERSHEY_TRIPLEX | cv2.FONT_ITALIC, SCALE, COLOR, THICKNESS)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
