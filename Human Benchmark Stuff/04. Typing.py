from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import pyautogui

characters = []

# Add the directory containing the WebDriver to the PATH
chrome_driver_path = r"C:\Users\School account\Downloads\Other\Python things\Chrome webdriver\chromedriver-win64\chromedriver.exe"
os.environ['PATH'] += os.pathsep + chrome_driver_path

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# URL of the website
url = 'https://humanbenchmark.com/tests/typing'  # Replace this with the URL of the website you want to scrape

# Configure Chrome options
chrome_options = Options()
# Commenting out the headless mode to show the WebDriver
# chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)

# Set up the Chrome webdriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the webpage
driver.get(url)

# Wait for the page to load (you may need to adjust the time based on the page load speed)
driver.implicitly_wait(10)  # Waits for 10 seconds for elements to appear

# Find elements with class "letters" (assuming it loads dynamically)
letters_elements = driver.find_elements(By.CLASS_NAME, 'letters')

if letters_elements:
    # Extract text content of each element found
    for element in letters_elements:
        characters.append(element.text)

    # # Join the characters list into a string
    # words_to_type = ' '.join(characters)

    # Print the words
    print("Words to type:", characters)

    # Simulate typing using PyAutoGUI
    time.sleep(10)  # Adding a delay before typing starts (adjust as needed)
    pyautogui.press(characters, interval = 0)  # Typing out the words

else:
    print("No elements with class 'letters' found.")

time.sleep(5)
# Keep the browser window open for viewing
pyautogui.alert('PRESSING OK CLOSES BROWSER!')

# Close the browser session
driver.quit()
