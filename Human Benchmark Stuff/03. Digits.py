import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Define driver path
chrome_driver_path = r"C:\Users\School account\Downloads\Other\Python things\Chrome webdriver\chromedriver-win64\chromedriver.exe"

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# URL of the website
url = 'https://humanbenchmark.com/tests/number-memory'  # Replace this with the URL of the website you want to scrape

service = Service(chrome_driver_path)

# Set up the Chrome webdriver
driver = webdriver.Chrome(None, service)

# Open the webpage
driver.get(url)

# init
run_amount = 50 # amount of times to run (edit to liking)
ran = 0

# wait to run program
pyautogui.alert("""1. Wait for the page to load
2. Decline/Accept the cookies and put the browser into fullscreen (important for larger run amounts)
3. REMOVE ALL ADS!!!! VERY IMPORTANT! (otherwise it'll error trying to click the buttons)
4. Click ok to start the program
5. Watch it go to work!
""", 'INSTRUCTIONS!!', 'I have read and agree.')


# find the start button
Start = driver.find_element(By.XPATH, '//button[text()="Start"]')
Start.click()

while ran <= run_amount:
    number = None
    submit_button = None
    next_button = None
    
    # finding number
    while not number:
        try:
            number = driver.find_element(By.CLASS_NAME, 'big-number').text
        except NoSuchElementException:
            sleep(0.1)

    # find the sumbit button --> timer
    while not submit_button:
        try:
            submit_button = driver.find_element(By.XPATH, '//button[text()="Submit"]')
        except NoSuchElementException:
            sleep(0.1)

    # write the number
    pyautogui.write(number)
    print(f'Entered number: {number}')
    print(f'This number is {len(number)} digits')
    print()

    # Submit it
    submit_button.click()
    
    # find the next button
    while not next_button:
        try:
            next_button = driver.find_element(By.XPATH, '//button[text()="NEXT"]')
        except NoSuchElementException:
            sleep(0.1)

    # Click next button
    next_button.click()
    
    ran += 1

pyautogui.alert('Click ok to close browser!')
driver.quit()
