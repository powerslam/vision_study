import cv2

img = cv2.imread('img.jpg')

# img[세로 범위, 가로 범위]
crop = img[100:200, 200:400] # 세로 100 ~ 200 / 가로 200 ~ 400

cv2.imshow('img1', img)
cv2.imshow('crop', crop)

# 이러면 자른 이미지를 원본에 붙여넣을 수 있다
# 단, 이 때 붙여넣는 공간의 크기는 crop의 공간의 크기와 일치해야 함
img[100:200, 400:600] = crop
cv2.imshow('img2', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
