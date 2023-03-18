import cv2
import numpy as np

point_list = []
src_img = cv2.imread('poker.jpg')

COLOR = (255, 0, 255) # 마젠타
THICKNESS = 3
drawing = False # 선을 그릴지 여부

def mouse_handler(event, x, y, flags, param):
    global drawing
    dst_img = src_img.copy()

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True # 선을 그리기 시작
        point_list.append((x, y))

    if drawing:
        prev_point = None # 직선의 시작점
        for point in point_list:
            cv2.circle(dst_img, point, 15, COLOR, cv2.FILLED)
            
            if prev_point:
                cv2.line(dst_img, prev_point, point, COLOR, THICKNESS, cv2.LINE_AA)

            prev_point = point

        next_point = (x, y)
        if len(point_list) == 4:
            show_result() # 결과 출력
            next_point = point_list[0] # 첫 번째 클릭한 지점
            drawing = False

        cv2.line(dst_img, prev_point, next_point, COLOR, THICKNESS, cv2.LINE_AA)
    cv2.imshow('img', dst_img) # 이래야 덮어쓰기 가능

def show_result():
    w, h = 530, 710
    src = np.float32(point_list)
    dst = np.array([[0, 0], [w, 0], [w, h], [0, h]], dtype=np.float32)

    matrix = cv2.getPerspectiveTransform(src, dst) # src -> dst 를 위한 matrix를 계산함
    result =  cv2.warpPerspective(src_img, matrix, (w, h)) # matrix 대로 변환을 함
    cv2.imshow('result', result)

# img 라는 이름의 윈도를 먼저 생성
# 마우스 이벤트를 처리하기 위한 핸들러 사용
cv2.namedWindow('img') 
cv2.setMouseCallback('img', mouse_handler) # img 라는 윈도우에 마우스 콜백 적용
cv2.imshow('img', src_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
