import sys
import time
from datetime import datetime

import keyboard
import pyautogui
import win32api
import win32con

red_button_coordinates = (1050, 920)
battle_button_coordinates = (940, 920)
ok_button_coordinates = (940, 850)
end_of_battle_coordinates = (921, 239)

red_button_color = (255, 120, 67)
yellow_button_color = (246, 201, 81)
win_screen_color = (255, 226, 64)

total_attempts = 0
isPaused = False


def click(coordinates):
    mouse_pos = win32api.GetCursorPos()
    win32api.SetCursorPos(coordinates)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    win32api.SetCursorPos(mouse_pos)


print("---------------------------------------------")
print("Idle Heroes Campaign Bot v1.21 by Supergato#1413")
print("Press 'Ctrl + s' to start")
print("Hold 'Ctrl + p' to pause/resume")
print("Hold 'Ctrl + q' to end the process")
print("---------------------------------------------")
print("")

keyboard.wait('ctrl+s')

print("Starting program")

while True:
    time.sleep(0.3)

    if not isPaused:

        # Pressing the start battle button
        if pyautogui.pixelMatchesColor(*red_button_coordinates, red_button_color, tolerance=10):
            click(red_button_coordinates)

        # Pressing the battle button in the hero deployment screen
        if pyautogui.pixelMatchesColor(*battle_button_coordinates, yellow_button_color, tolerance=10):
            click(battle_button_coordinates)

        # Checking if the battle was won
        if pyautogui.pixelMatchesColor(*end_of_battle_coordinates, win_screen_color, tolerance=10):
            now = datetime.now()
            print(now.strftime("%H:%M:%S"), "Level beaten")

        # Pressing the ok button
        if pyautogui.pixelMatchesColor(*ok_button_coordinates, yellow_button_color, tolerance=10):
            click(ok_button_coordinates)

            now = datetime.now()
            total_attempts += 1
            print(now.strftime("%H:%M:%S"), "Total attempts:", total_attempts)

    # Check if user pauses the process
    if keyboard.is_pressed('ctrl+p'):
        if isPaused:
            print("Resuming the process")
        else:
            print("Pausing the process")
        isPaused = not isPaused

    # Check if program wants to be closed
    if keyboard.is_pressed('ctrl+q'):
        print("Exiting program")
        sys.exit()
