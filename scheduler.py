from JoinMeeting import joinzoommeeting
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


chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

MyMeeting="https://us04web.zoom.us/j/7340158029?pwd=WU5kcXJJTlUwMjl4OGpGZ3liQTArZz09"
def scheduler():
    def regularmeet(x,day,t=None):
        
        week = datetime.datetime.today().weekday()
        if t is not None and week in day:
            print("hi")
            schedule.every().day.at(t).do(joinzoommeeting,x,chrome_path)
    meetings=[[MyMeeting,[6,5,1,2,3,4,0],"21:04"]]
    for meeting in meetings:
        regularmeet(meeting[0],meeting[1],meeting[2])