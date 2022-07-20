from datetime import datetime
from PIL import ImageGrab
import numpy as np
import cv2
import pywin32_system32
# from pywin32_system32 import win32api
from win32api import GetSystemMetrics
cap  = cv2.VideoCapture(0)

def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

# width = GetSystemMetrics(0)
# height = GetSystemMetrics(1)
# time_stamp = datetime.now().strftime('%Y-%M-%d-%H-%M-%s')
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(
    'Saved recording.mp4', fourcc, 20.0, (1920, 1080))

# print(width , height)


while True:
    img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow("Secret capture", img_final)
    captured_video.write(img_final)
    if cv2.waitKey(10) == ord('p'):
        break
