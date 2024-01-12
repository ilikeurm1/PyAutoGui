from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard
import time
import pyautogui
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome webdriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# URL of the website
url = 'https://humanbenchmark.com/tests/chimp'  # Replace this with the URL of the website you want to scrape

# Open the webpage
driver.get(url)

driver.implicitly_wait(10)

numbers = 4
while True:
    for i in range(1, numbers + 1):
        el = driver.find_element(By.XPATH, f'//div[@data-cellnumber="{i}"]')
        el.click()

    time.sleep(0.3) 
    
    if numbers < 40:
        # Go to the next level
        continue_button = driver.find_element(By.XPATH, '//button[text()="Continue"]')
        continue_button.click()
        
        time.sleep(0.1)
    else:
        break
        
    numbers += 1

pyautogui.alert('When clicking ok the browser will close! So do anything you want to do now before it does!')
driver.quit()  # Close the browser session after use
