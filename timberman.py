import torch
from matplotlib import pyplot as plt

import pyautogui
import cv2
import numpy as np

from ultralytics import YOLO

model = YOLO('yolov8n.pt')


# 録画フレーム
while True:
    screen =pyautogui.screenshot()
    screen_array=np.array(screen)
    
    # 画像のキャプチャ範囲
    cropped_region=screen_array[25:625,1122:,:]
    # rgbからbgrに変換 (Opencvが読み取りやすいように)
    corrected_colors=cv2.cvtColor(cropped_region,cv2.COLOR_RGB2BGR)
    
    results=model(corrected_colors)
    
    cv2.imshow('YOLO',np.squeeze(results.render()))
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cv2.destroyAllWindows()
    
    
    