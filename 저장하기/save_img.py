import cv2

img = cv2.imread('d:\\Project\\vision\\img.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 이 예제에서는 사진 한 번 보여주고 했는데
# 안 보여주고 imread 하고 다시 저장할 수 있다
res1 = cv2.imwrite('img_save1.jpg', img)
res2 = cv2.imwrite('img_save2.jpg', img)
print(res1, res2)
