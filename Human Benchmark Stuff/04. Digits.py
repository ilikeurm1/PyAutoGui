import pyautogui
import pytesseract
from PIL import ImageOps
import re
from time import sleep

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# init
run_amount = 10
counter = 0
timer = 0
found = []

# Define the coordinates for the region to search for the number
start_x, start_y = 207, 529
end_x, end_y = 1877, 670

# click start button
pyautogui.click(980, 855)

while counter != run_amount:
    sleep(.5)
    # Function to preprocess the image by applying a threshold
    def preprocess_image(img, threshold_value):
        # Convert the image to grayscale
        grayscale_img = ImageOps.grayscale(img)
        # Apply thresholding to enhance number recognition
        thresholded_img = ImageOps.invert(grayscale_img.point(lambda p: p > threshold_value and 255))
        return thresholded_img

    # Set threshold value for image preprocessing
    threshold_value = 150  # Adjust this threshold value as needed

    # Get the screenshot of the defined region
    screenshot = pyautogui.screenshot(region=(start_x, start_y, end_x - start_x, end_y - start_y))

    # Convert the screenshot to grayscale and apply thresholding
    preprocessed_screenshot = preprocess_image(screenshot, threshold_value)

    # show preprocessed image
    preprocessed_screenshot.show()

    # Perform OCR on the preprocessed image
    text = pytesseract.image_to_string(preprocessed_screenshot)

    # Use regular expression to find numbers in the text
    numbers_found = re.findall(r'\d+', text)

    # Print the numbers found
    if numbers_found:
        number = numbers_found[0]
        print('THIS IS THE NUMBER THAT I FOUND:')
        print(number)

        # add each single number to a list
        for x in number:
            found.append(str(x))

        print("Numbers found:")
        print(found)
        sleep(len(found) + 1)
        pyautogui.typewrite(found, interval=0.1)
        sleep(1)
        pyautogui.press('enter', presses=2, interval=0.5)

        # clear lists for new number
        numbers_found.clear()
        found.clear()

        # add to counter to make it end eventually
        counter += 1
    else:
        print("No numbers found in the specified region.")
        break
    





# ================================== UNDER NEATH THIS LINE THERE IS TESTING CODE ==================================




# sleep(.5)

# # Function to preprocess the image by applying a threshold
# def preprocess_image(img, threshold_value):
#     # Convert the image to grayscale
#     grayscale_img = ImageOps.grayscale(img)
#     # Apply thresholding to enhance number recognition
#     thresholded_img = ImageOps.invert(grayscale_img.point(lambda p: p > threshold_value and 255))
#     return thresholded_img

# # Set threshold value for image preprocessing
# threshold_value = 150  # Adjust this threshold value as needed

# # Get the screenshot of the defined region
# screenshot = pyautogui.screenshot(region=(start_x, start_y, end_x - start_x, end_y - start_y))

# # Convert the screenshot to grayscale and apply thresholding
# preprocessed_screenshot = preprocess_image(screenshot, threshold_value)

# # show preprocessed image
# preprocessed_screenshot.show()

# # Perform OCR on the preprocessed image
# text = pytesseract.image_to_string(preprocessed_screenshot)

# print("Text extracted after thresholding:")
# print(text)

# # Use regular expression to find numbers in the text
# numbers_found = re.findall(r'\d+', text)

# # Print the numbers found
# if numbers_found:
#     number = numbers_found[0]
#     print('THIS IS THE NUMBER THAT I FOUND:')
#     print(number)

#     # add each single number to a list
#     for x in number:
#         found.append(str(x))

#     print("Numbers found:")
#     print(found)
#     sleep(len(found) + 1)
#     pyautogui.typewrite(found, interval=0.1)
#     sleep(1)
#     pyautogui.press('enter', presses=2, interval=0.5)

#     # clear lists for new number
#     numbers_found.clear()
#     found.clear()

#     # add to counter to make it end eventually
#     counter += 1
# else:
#     print("No numbers found in the specified region.")
#     # break
