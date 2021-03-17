from pyautogui import *
import pyautogui
import time
import keyboard
import win32api
import win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(5.00) #This pauses the script for 5 sec
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:
    t = 0;
    if pyautogui.pixel(1734, 936) [0] == 115:
        click(1700, 950);
        t += 1;
        if (t == 1):
            if pyautogui.pixel(1700, 950) [1] == 159:
                click(310, 13);
                t -= 1;