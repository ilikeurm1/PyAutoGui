import pyautogui
import time

# Define the coordinates for the board
Board = [
    ((780, 480), (980, 480), (1180, 480)),

    ((780, 680), (980, 680), (1180, 680)),

    ((780, 880), (980, 880), (1180, 880))
]

Sequence = []
Passes = 1

# Function to check if a coordinate has turned white
def is_white(coord):
    x, y = coord
    pixel_color = pyautogui.pixel(x, y)
    # Check if the pixel color is close to white (you may need to adjust the RGB values)
    return pixel_color[0] > 200 and pixel_color[1] > 200 and pixel_color[2] > 200

# Function to check the board for white coordinates
def check_board():
    global Sequence
    global Passes
    wait = (100, 100)
    timer = time.time() - 5
    while len(Sequence) != Passes:
        for row in Board:
            for coord in row:
                if is_white(coord):
                    added = time.time()
                    print(f"FOUND COORDINATE: {coord}")
                    if coord != wait or added - timer > 0.1:
                        wait = coord
                        timer = time.time()
                        Sequence.append(coord)
                        print(f"Added {coord} to Sequence")
                        

# Function to click on the recorded sequence of coordinates
def click_sequence():
    for coord in Sequence:
        pyautogui.click(coord)
        print(f'Clicked on {coord}')
        time.sleep(.1)

# click start button
pyautogui.click(980, 855)
pyautogui.moveTo(100, 100)

# Main loop to continuously check the board
while Passes != 100:
    time.sleep(Passes* .5)
    check_board()
    print(Sequence)
    time.sleep(1)
    click_sequence()
    pyautogui.moveTo(100, 100)
    Passes += 1
    print(Sequence)
    time.sleep(.4)
