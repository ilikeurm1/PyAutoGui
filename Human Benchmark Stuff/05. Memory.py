from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome webdriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

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

    num_squares += 1
    ran += 1

pyautogui.alert('By clicking ok the browser will close. So do anything you want before clicking it!')
driver.quit()
