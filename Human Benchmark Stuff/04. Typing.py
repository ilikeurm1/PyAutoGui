from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pyautogui
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome webdriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# URL of the website
url = 'https://humanbenchmark.com/tests/typing'

# Open the webpage
driver.get(url)

# Wait for the page to load
driver.implicitly_wait(10)

# Find elements with class "letters"
letters_elements = None
while not letters_elements:
    try:
        letters_elements = driver.find_elements(By.CLASS_NAME, 'letters')
    except NoSuchElementException as e:
        time.sleep(.1)


if letters_elements:
    characters = []
    
    # Extract text content of each element found
    for element in letters_elements:
        characters.append(element.text)

    # Print the words
    print("Words to type:", characters)

    # Simulate typing using PyAutoGUI
    time.sleep(10)  # Adding a delay before typing starts
    pyautogui.write(characters[0])  # Typing out the words

time.sleep(5)

# Keep the browser window open for viewing
pyautogui.alert('PRESSING OK CLOSES BROWSER!')

# Close the browser session
driver.quit()
