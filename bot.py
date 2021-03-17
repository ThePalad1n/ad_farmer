from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#RGB:(156, 29, 151)
#XTL: X: 1656
#YTL: Y:  944
#XBL: X: 1654
#YBL: Y: 1019
#XTR: X: 1841
#YTR: Y:  951
#XBR: X: 1837
#YBR:Y:  951

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(1.00) #This pauses the script for 1 sec
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(1700, 950) [0] == 156:
        click(1700, 950);