import pyautogui
from time import sleep, time

def Clicker(x, y, c):
    while True:
        pixel_color = pyautogui.pixel(x, y)
        if pixel_color == c:
            pyautogui.click(x, y)
            break
    start = time()
    # Wait for the pixel to turn green before the second click
    
    # click again to restart
    pyautogui.click(x, y)
    
    end = time()
    print(f"Click performed after: {round(100 * (end - start), 2)} ms.")


# Set your coordinates (x, y) and the expected color in RGB format (R, G, B)
x, y, c = 980, 270, (75, 219, 106)

sleep(2)

# Perform the first click
pyautogui.click(x, y)

# Main loop
for _ in range(5):
    Clicker(x, y, c)
