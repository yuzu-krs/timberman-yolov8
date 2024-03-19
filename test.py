import cv2

# 画面をキャプチャ
cap = cv2.VideoCapture(0)  # 0はwebカメラを指しますが、必要に応じて適切なソースを指定してください
ret, frame = cap.read()

# 切り取る範囲の座標
x, y, width, height = 100, 100, 200, 200  # 例として、左上が(100, 100)で幅と高さがそれぞれ200ピクセルの領域を切り取るとします

# 切り取り
cropped_frame = frame[y:y+height, x:x+width]

# 画面を表示
cv2.imshow("Cropped Frame", cropped_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ここでcropped_frameをYOLOv8に入力して物体検出を行います