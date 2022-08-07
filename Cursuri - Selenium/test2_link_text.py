from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

# # deschidem o pagina
# chrome.get('https://formy-project.herokuapp.com')
#
#
# # selectors by link
# chrome.find_element(By.LINK_TEXT, 'Autocomplete').click()

chrome.get('https://formy-project.herokuapp.com')

# selectors by partial link test
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Enabled').click()

sleep(10)
chrome.quit()