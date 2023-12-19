import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Define driver path
chrome_driver_path = r"C:\Users\School account\Downloads\Other\Python things\Chrome webdriver\chromedriver-win64\chromedriver.exe"

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# URL of the website
url = 'https://humanbenchmark.com/tests/verbal-memory'  # Replace this with the URL of the website you want to scrape

service = Service(chrome_driver_path)

# Set up the Chrome webdriver
driver = webdriver.Chrome(None, service)

# Open the webpage
driver.get(url)

# init
run_amount = 5000 # amount of times to run (edit to liking)
ran = 0

# wait to run program
pyautogui.alert("""1. Wait for the page to load
2. Decline/Accept the cookies and put the browser into fullscreen
3. REMOVE ALL ADS!!!! VERY IMPORTANT!
4. Click ok to start the program
5. Watch it go to work!
""", 'INSTRUCTIONS!!', 'I have read and agree.')


# find the 
Start = driver.find_element(By.XPATH, '//button[text()="Start"]')
Start.click()
sleep(.2)


# get seen and new buttons
seen_button = driver.find_element(By.XPATH, '//button[text()="SEEN"]')
new_button = driver.find_element(By.XPATH, '//button[text()="NEW"]')

# store seen words
words = set()

while ran != run_amount:
    # get shown word
    word = driver.find_element(By.CLASS_NAME, 'word').text
    
    if word in words:
        seen_button.click()
    else:
        new_button.click()
        words.add(word)
    
    ran += 1

print(f'These were all words that were encountered: {words}')
print(f'There were {len(words)} unique words out of the {run_amount} that were shown')
print(f"That means that on average every 1 in {round(run_amount / len(words), 5)} was a new word (this should be pretty close to 1 in 2)")

pyautogui.alert('Click ok to close browser!')
driver.quit()
