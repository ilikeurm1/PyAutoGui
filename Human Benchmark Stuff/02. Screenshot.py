# import pyautogui
# from time import sleep


# counter = 0
# image = r'C:\Users\School account\Documents\Coding\Scripting\Pyton\Personal\Matthijs-Projects\Learning PyAutoGui\Pictures\Aimer.png'
# threshold = 0.7

# def find_and_click_image(image_path, confidence_threshold):
#     try:
#         x, y = pyautogui.locateCenterOnScreen(image_path, confidence=confidence_threshold)
#         if x is not None and y is not None:
#             pyautogui.click(x, y)
#             print(f"Clicked on the image found at coordinates: ({x}, {y})")
#         else:
#             print("Image not found on the screen.")
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")

# sleep(5)

# while counter != 31:
#     find_and_click_image(image, threshold)
#     counter += 1


import pyautogui
from time import sleep
import cv2
import numpy as np
import mss
from PIL import Image

counter = 0
image_path = r'C:\Users\School account\Documents\Coding\Scripting\Pyton\Personal\Matthijs-Projects\Learning PyAutoGui\Pictures\Aimer.png'
threshold = 0.7

def find_and_click_image(image_path, confidence_threshold):
    try:
        with mss.mss() as sct:
            # Take a screenshot
            monitor = sct.monitors[1]  # Change the index based on your screen setup
            img = np.array(sct.grab(monitor))

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        template = cv2.imread(image_path, cv2.IMREAD_COLOR)  # Load image in color

        # Convert image to grayscale
        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        h, w = template_gray.shape[::-1]

        res = cv2.matchTemplate(img_rgb, template_gray, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= confidence_threshold)

        if len(loc[0]) > 0 and len(loc[1]) > 0:
            # Click on the first found location
            x, y = loc[1][0] + w // 2, loc[0][0] + h // 2
            pyautogui.click(x, y)
            print(f"Clicked on the image found at coordinates: ({x}, {y})")
        else:
            print("Image not found on the screen.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

sleep(5)

while counter != 31:
    find_and_click_image(image_path, threshold)
    counter += 1
