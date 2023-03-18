import cv2

# 해당 경로의 파일 읽어오기
img_color = cv2.imread('img.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
img_unchanged = cv2.imread('img.jpg', cv2.IMREAD_UNCHANGED)

# <image>.shape === tuple(높이, 너비, 채널 수)
print(img_color.shape)
print(img_gray.shape)
print(img_unchanged.shape)

# imread 옵션들
# 1. cv2.IMREAD_COLOR : 컬러 이미지 / 투명 무시 (기본값)
# 2. cv2.IMREAD_GRAYSCALE : 흑백 이미지
# 3. CV2.IMREAD_UNCHANGED : 컬러 이미지 / 투명 포함

# img_color 라는 이름의 창에 img_color 를 표시
cv2.imshow('img_color', img_color)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_unchanged', img_unchanged)
key = cv2.waitKey(0) # 리턴값으로 입력한 키의 아스키 코드 값을 전달한다
# 지정된 시간 동안 사용자 키 입력 대기 0 이면 무한대기
# ms 단위이다.
# 안하면 바로 창이 꺼짐
print('You input', key)
cv2.destroyAllWindows() # 모든 창 닫기
