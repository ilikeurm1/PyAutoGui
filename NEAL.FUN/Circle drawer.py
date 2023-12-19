import pyautogui
from time import sleep

def draw_square(center):
    # define x and y and r
    x = center[0]
    y = center[1]
    r = 300

    # define points in "square"
    top = (x, y - r)
    bottom = (x, y + r)
    right = (x + r, y)
    left = (x - r, y)

    # Mouse down before dragging
    pyautogui.mouseDown()

    # Drag to all points in square in order
    pyautogui.moveTo(top)
    pyautogui.dragTo(right)
    sleep(0.1)  # Small delay between drag operations
    pyautogui.dragTo(bottom)
    sleep(0.1)
    pyautogui.dragTo(left)
    sleep(0.1)
    pyautogui.dragTo(top)

    # Mouse up after completing the square
    pyautogui.mouseUp()

Center = (991, 550)

draw_square(Center)
