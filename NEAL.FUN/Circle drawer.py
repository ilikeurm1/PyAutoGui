import pyautogui
from time import sleep as s

def draw_square(t, r, b, l):
    # Mouse down before dragging
    pyautogui.moveTo(t)
    pyautogui.mouseDown()

    # Drag to all points in square in order
    pyautogui.moveTo(r)
    pyautogui.moveTo(b)
    pyautogui.moveTo(l)
    pyautogui.moveTo(t)

    # Mouse up after completing the square
    pyautogui.mouseUp()

Center = (1300, 726)

# define x and y and r
x = Center[0]
y = Center[1]
r = 550

# define points in "square"
top = (x, y - r)
bottom = (x, y + r)
right = (x + r, y)
left = (x - r, y)

s(4)

draw_square(top, right, bottom, left)

# import pyautogui
# import math
# from time import sleep as s

# # Center point
# center_x, center_y = 1300, 726
# radius = 550

# # Calculate the points of the circle using trigonometry
# points = []
# for angle in range(-90, 271, 90):  # Increase step for more or fewer points
#     x = center_x + int(radius * math.cos(math.radians(angle)))
#     y = center_y + int(radius * math.sin(math.radians(angle)))
#     points.append((x, y))

# s(4)

# # Move the mouse and draw the circle
# pyautogui.moveTo(points[0])
# pyautogui.mouseDown()

# for point in points:
#     pyautogui.moveTo(point)

# pyautogui.mouseUp()
