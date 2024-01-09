# import pyautogui
# from time import sleep as s

# def draw_square(t, r, b, l):
#     # Mouse down before dragging
#     pyautogui.moveTo(t)
#     pyautogui.mouseDown()

#     # Drag to all points in square in order
#     pyautogui.moveTo(r)
#     pyautogui.moveTo(b)
#     pyautogui.moveTo(l)
#     pyautogui.moveTo(t)

#     # Mouse up after completing the square
#     pyautogui.mouseUp()

# # define the center of your circle (this might be a bit off to the left as im using opera gx with a sidebar)
# size = pyautogui.size()

# if size[1] == 1080:
#     # 1080p monitors
#     Center = (991, 550)
#     Pass = True
#     r = 350
# elif size[1] == 1440:
#     # 1440p monitors
#     Center = (1300, 726)
#     Pass = True
#     r = 550
# else:
#     pyautogui.alert('Sorry, i dont support this resolution, please change you moonitor to: 1920x1080p or 2560x1440p', 'ERROR', 'I understand')
#     Pass = False

# if Pass:
#     # define x and y and r
#     x = Center[0]
#     y = Center[1]

#     # define points in "square"
#     top = (x, y - r)
#     bottom = (x, y + r)
#     right = (x + r, y)
#     left = (x - r, y)

#     s(4)

#     # draw circle
#     draw_square(top, right, bottom, left)
# else:
#     pass


"""
===========================================================================================================================================================================================
================================================================================= UNDER IS  OTHER VERSION =================================================================================
===========================================================================================================================================================================================
"""

import pyautogui
import math
from time import sleep as s

# define the center of your circle (this might be a bit off to the left as im using opera gx with a sidebar)
size = pyautogui.size()

if size[1] == 1080:
    # 1080p monitors
    Center = (991, 550)
    Pass = True
    r = 350
elif size[1] == 1440:
    # 1440p monitors
    Center = (1300, 726)
    Pass = True
    r = 550
else:
    pyautogui.alert('Sorry, i dont support this resolution, please change you moonitor to: 1920x1080p or 2560x1440p', 'ERROR', 'I understand')
    Pass = False

if Pass:
    # define x and y and r
    x = Center[0]
    y = Center[1]

    # Calculate the points of the circle using trigonometry
    points = []
    for angle in range(-90, 271, 90):  # Increase step for more or fewer points
        point_x = x + int(r * math.cos(math.radians(angle)))
        point_y = y + int(r * math.sin(math.radians(angle)))
        points.append((point_x, point_y))

    s(4)

    # Move the mouse and draw the circle
    pyautogui.moveTo(points[0])
    pyautogui.mouseDown()

    for point in points:
        pyautogui.moveTo(point)

    pyautogui.mouseUp()
else:
    pass