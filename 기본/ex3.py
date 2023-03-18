import cv2

cap = cv2.VideoCapture(0) # 0번째 카메라 장치

if not cap.isOpened(): # 카메라가 열리지 않은 경우
    exit() # 프로그램 종료

while True: # 동영상과 달리 제한된 시간이 없기 때문에
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('camera', frame)

    if cv2.waitKey(1) == ord('q'):
        print('사용자 입력에 의해 종료되었습니다')
        break

cap.release() # 열었던 카메라 종료
cv2.destroyAllWindows()
