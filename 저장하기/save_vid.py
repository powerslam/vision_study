import cv2

cap = cv2.VideoCapture('d:\\Project\\vision\\video.mp4')

# 동영상 코덱 정의
# 원래 DIVX를 각각 적어서 4개를 넘거야 하니깐 *을 이용해 풀어서 넘기는 것
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fps_fast = fps * 2

out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))
out_fast = cv2.VideoWriter('output_fast.avi', fourcc, fps_fast, (width, height))
# 저장 파일명, 코덱, fps, 크기

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    out.write(frame) # 영상만 저장 / 소리는 X
    out_fast.write(frame)

    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()
