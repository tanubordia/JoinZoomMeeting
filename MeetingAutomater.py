from scheduler import scheduler
from camerafeed import virtualCamera
import pyautogui as pyg
import webbrowser as wb
import datetime
import time
import click
import os
import schedule
import cv2
import pyvirtualcam
import numpy as np



# wait for 10 secpip install sched


scheduler()
while True:
    schedule.run_pending()
    time.sleep(1)
