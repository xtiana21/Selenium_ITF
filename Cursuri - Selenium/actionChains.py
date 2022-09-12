
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#initializam un browser
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()

# deschidem o pagina
chrome.get('https://www.sendspace.com/login.html')
time.sleep(10)
login_button = chrome.find_element(By.XPATH, "//input[text()='Log In']")
actions = ActionChains(chrome)
actions.move_to_element(login_button).perform()
time.sleep(10)
login_button.click()

chrome.quit()

