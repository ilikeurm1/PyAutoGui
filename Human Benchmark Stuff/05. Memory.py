from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import keyboard
import time
import pyautogui

# Start button
start_button = 'p'

# Define driver path
chrome_driver_path = r"C:\Users\School account\Downloads\Other\Python things\Chrome webdriver\chromedriver-win64\chromedriver.exe"

# Initialize the Chrome WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(None, service)

# URL of the website
url = 'https://humanbenchmark.com/tests/memory'  # Replace this with the URL of the website you want to scrape

# Open the webpage
driver.get(url)


run_amount = 100 # edit to liking
ran = 0
num_squares = 3


pyautogui.alert('Please wait for the page to load! (also put it in fullscreen!)')

while ran != run_amount:
    active_elements = []
    while len(active_elements) != num_squares:
        active_elements = driver.find_elements(By.CSS_SELECTOR, 'div.active')
    
    time.sleep(2)
    
    for element in active_elements:
        element.click()

    time.sleep(1)
        
    # break out of loop
    if keyboard.is_pressed(start_button):
        break

    num_squares += 1
    ran += 1

pyautogui.alert('By clicking ok the browser will close. So do anything you want before clicking it!')
driver.quit()
