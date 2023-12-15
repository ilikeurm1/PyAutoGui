import pyautogui
import time

# Coordinates list with x and y coordinates in tuples
coordinates = [
    (0, 1079),
    (900, 500),
    (900, 100),
    # Add more coordinates as needed
]

def click_coordinates(coords):
    pyautogui.alert(f'''when pressing OK your mouse will go to these coords:
{coords}''') 
    # Iterate through the coordinates and click each one
    for coord in coords:
        # Move the mouse to the coordinates and click
        pyautogui.click(coord[0], coord[1])
        time.sleep(0.1)  # Optional delay between clicks (adjust as needed)

click_coordinates(coordinates)