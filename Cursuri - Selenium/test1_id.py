# initializam un browser
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com/form')     #deschide o pagina

# cream o variabila pentru 'first name'
first_name = chrome.find_element(By.ID, 'first-name')

# adaugam un nume in field-ul first name
first_name.send_keys('Cristiana')
first_name.clear()                       # Stergen elementul anterior
first_name.send_keys('Marian')

# cream variabila pt last_name si adaugam noi un  nume
last_name = chrome.find_element(By.ID, 'last-name')
last_name.send_keys('Marin')


sleep(3)
chrome.quit()


