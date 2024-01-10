import pyautogui
from time import sleep as s

points = []

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

# define the center of your circle (this might be a bit off to the left as im using opera gx with a sidebar)
size = pyautogui.size()

browser = pyautogui.confirm('What browser are you using?', 'Browser', ['Opera gx', 'Chrome', 'None of above'])

if size[1] == 1080:
    # 1080p monitors
    r = 350
    if browser == 'Opera gx':
        Center = (991, 550)
        Pass = True
    elif browser == 'Chrome':
        Center = (960, 565)
        Pass = True
    else:
        pyautogui.alert("Sorry, i don't support this browser yet, please use one listed in the list!", 'Browser Support Error', 'I understand')
        Pass = False

elif size[1] == 1440:
    # 1440p monitors
    r = 550
    if browser == 'Opera gx':
        Center = (1300, 726)  
        Pass = True
    elif browser == 'Chrome':
        pyautogui.alert('This is a temporary error, i guess i might be able to guess the coords of of the change in coords in 1080p but im too lazy to do that rn.')
    else:
        pyautogui.alert("Sorry, i don't support this browser yet, please use one listed in the list!", 'Browser Support Error', 'I understand')
        Pass = False
else:
    pyautogui.alert('Sorry, i dont support this resolution, please change you moonitor to: 1920x1080p or 2560x1440p', 'Resolution Error', 'I understand')
    Pass = False

if Pass:
    # define x and y and r
    x = Center[0]
    y = Center[1]

    # define points in "circle" (square)
    top = (x, y - r)
    right = (x + r, y)
    bottom = (x, y + r)
    left = (x - r, y)

    # points.append(top)
    # points.append(right)
    # points.append(bottom)
    # points.append(left)

    # for coord in points:
    #     print(coord) # print out what the coords
    
    s(4)

    # draw circle
    draw_square(top, right, bottom, left)
    pyautogui.moveTo(Center)
else:
    pass


"""
===========================================================================================================================================================================================
================================================================================= UNDER IS  OTHER VERSION =================================================================================
===========================================================================================================================================================================================
"""

# import pyautogui
# import math
# from time import sleep as s

# # define the center of your circle (this might be a bit off to the left as im using opera gx with a sidebar)
# size = pyautogui.size()

# browser = pyautogui.confirm('What browser are you using?', 'Browser', ['Opera gx', 'Chrome', 'Not supported browser'])

# if size[1] == 1080:
#     # 1080p monitors
#     r = 350
#     if browser == 'Opera gx':
#         Center = (991, 551)
#         Pass = True
#     elif browser == 'Chrome':
#         Center = (961, 566)
#         Pass = True
#     else:
#         pyautogui.alert("Sorry, i don't support this browser yet, please use one listed in the list!", 'Browser Support Error', 'I understand')
#         Pass = False

# elif size[1] == 1440:
#     # 1440p monitors
#     r = 550
#     if browser == 'Opera gx':
#         Center = (1300, 726)  
#         Pass = True
#     elif browser == 'Chrome':
#         pyautogui.alert('This is a temporary error, i guess i might be able to guess the coords of of the change in coords in 1080p but im too lazy to do that rn.')
#     else:
#         pyautogui.alert("Sorry, i don't support this browser yet, please use one listed in the list!", 'Browser Support Error', 'I understand')
#         Pass = False
# else:
#     pyautogui.alert('Sorry, i dont support this resolution, please change you moonitor to: 1920x1080p or 2560x1440p', 'Resolution Error', 'I understand')
#     Pass = False

# if Pass:
#     # define x and y and r
#     x = Center[0]
#     y = Center[1]

#     # Calculate the points of the circle using trigonometry
#     points = []
#     for angle in range(0, 361, 90):  # Increase step for more or fewer points
#         point_x = x + int(r * math.cos(math.radians(angle)))
#         point_y = y + int(r * math.sin(math.radians(angle)))
#         points.append((point_x, point_y))

#     points.reverse() # Counter clockwise 
#     for coord in points:
#         print(coord) # print out what coords ill move to in order
#     s(4)

#     # Move the mouse and draw the circle
#     pyautogui.moveTo(points[0])
#     pyautogui.mouseDown()

#     for point in points:
#         pyautogui.moveTo(point)

#     pyautogui.mouseUp()
#     pyautogui.moveTo(Center)
# else:
#     pass