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

def joinzoommeeting(zoom_link,chrome_path):
    wb.register('chrome', None,wb.BackgroundBrowser(chrome_path))
    wb.get(using='chrome').open(zoom_link, new=2)
    time.sleep(10) # given time for the link to show app top-up window
    pyg.click(x=1000, y=265, clicks=1, interval=0, button='left') # click on open zoom.app option
    time.sleep(10)
    virtualCamera()