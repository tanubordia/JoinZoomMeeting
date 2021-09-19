import pyautogui as pyg
import webbrowser as wb
import datetime
import time
import click
import os
import schedule

chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
def joinzoommeeting(zoom_link,chrome_path):
    wb.register('chrome', None,wb.BackgroundBrowser(chrome_path))
    wb.get(using='chrome').open(zoom_link, new=2)
    time.sleep(10) # given time for the link to show app top-up window
    pyg.click(x=1000, y=265, clicks=1, interval=0, button='left') # click on open zoom.app option
    time.sleep(10) # wait for 10 secpip install sched
zoom_link="https://us05web.zoom.us/j/84511633580?pwd=VlgzZzlDNEVTWDlUL0RWZlZRMTFxQT09"

def regularmeet(x,t=None):
    
    week = datetime.datetime.today().weekday()
    if t is not None and week < 6:
        schedule.every().day.at(t).do(joinzoommeeting,x,chrome_path)

regularmeet(zoom_link,"11:30")

while True:
    schedule.run_pending()
    time.sleep(1)
