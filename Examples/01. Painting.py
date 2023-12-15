import pyautogui as pyg
from time import sleep

sleep(2)
distance = 300
while distance > 0:
    pyg.drag(distance, 0, duration=0.5)   # move right
    distance -= 4
    pyg.drag(0, distance, duration=0.5)   # move down
    pyg.drag(-distance, 0, duration=0.5)  # move left
    distance -= 4
    pyg.drag(0, -distance, duration=0.5)  # move up