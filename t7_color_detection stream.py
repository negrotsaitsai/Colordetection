import cv2
import numpy as np

cap = cv2.VideoCapture(0) #讀取影片

color_range = [np.array([35, 0, 0]), np.array([50, 255, 255])] #顏色範圍

while True:
    ret, frame = cap.read() #讀取每一幀

    draw = np.ones((frame.shape[0],frame.shape[1],3), np.uint8)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #色彩空間轉換BGR->HSV
    mask = cv2.inRange(hsv, color_range[0], color_range[1]) #色彩範圍二值化
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if mask[i][j] == 0: draw[i,j,:] = frame[i,j,:] #黑色部分還原
            else: draw[i,j,:] = (255, 0, 0) #白色部分當背景

    cv2.imshow('1.original', frame)
    cv2.imshow('2.mask', mask)
    cv2.imshow('3.draw', draw)

    if cv2.waitKey(1) & 0xFF == ord('q'): break #按Q跳出

cv2.waitKey(0) #等待按下任意鍵
cv2.destroyAllWindows()