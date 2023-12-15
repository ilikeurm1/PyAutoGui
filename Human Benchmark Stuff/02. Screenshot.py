import pyautogui
from time import sleep


counter = 0
image = r'C:\Users\School account\Documents\Coding\Scripting\Pyton\Personal\Matthijs-Projects\Mouse-movement\Pictures\Aimer.png'
threshold = 0.7

def find_and_click_image(image_path, confidence_threshold):
    try:
        x, y = pyautogui.locateCenterOnScreen(image_path, confidence=confidence_threshold)
        if x is not None and y is not None:
            pyautogui.click(x, y)
            print(f"Clicked on the image found at coordinates: ({x}, {y})")
        else:
            print("Image not found on the screen.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

sleep(5)

while counter != 31:
    find_and_click_image(image, threshold)
    counter += 1
