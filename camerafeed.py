import cv2
import pyvirtualcam
import numpy as np


def virtualCamera():
    cvCam = cv2.VideoCapture('VideoFeed.mp4')
    width = int(cvCam.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cvCam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    with pyvirtualcam.Camera(width, height, fps=40) as cam:
        frames=[]
        while True:
            _, frame = cvCam.read()
            if frame is None:
                break
            frames.append(frame)
            frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
            cam.send(frame)
            cam.sleep_until_next_frame()
            
        while True:            
            for frame in frames:
                frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
                cam.send(frame)
                cam.sleep_until_next_frame()
