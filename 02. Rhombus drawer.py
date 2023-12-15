import pyautogui
from time import sleep

radius = ''

while radius == '':
    try:
        # enter radius in pixels
        radius = int(pyautogui.prompt('Please enter the radius of your rhombus (in pixels), then position your mouse (you have 2 sec).'))
    except:
        continue

sleep(2)

start_x, start_y = pyautogui.position()


bottom_point = start_x, start_y
left_point = start_x - radius / 2, start_y - radius / 2
top_point = start_x, start_y - radius
right_point = start_x + radius / 2, start_y - radius / 2

pyautogui.dragTo(left_point)
pyautogui.dragTo(top_point)
pyautogui.dragTo(right_point)
pyautogui.dragTo(bottom_point)

