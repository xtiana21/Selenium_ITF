# initializam un browser
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

# deschidem o pagina
chrome.get('https://formy-project.herokuapp.com/form')

# scrie in primul element de tip input
chrome.find_element(By.TAG_NAME, 'input').send_keys('Cris')

# cream o variabila pentru lista elementelor de tip input
lista_elemente_input = chrome.find_elements(By.TAG_NAME, 'input')

# Scriem in al 3 lea input de pe pagina
lista_elemente_input[2].send_keys('Ana')




sleep(5)
chrome.quit()