from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

''' Alegeti cate 3 elemente din fiecare tip de selector din urmatoarele categorii:

●	Id
●	Link text
●	Partial link text
●	Name
●	Tag* 
●	Class name*'''

# By.ID

chrome.get('https://formy-project.herokuapp.com/autocomplete')
chrome.find_element(By.ID, 'autocomplete').send_keys('Bucharest')

chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
chrome.find_element(By.ID, 'datepicker').send_keys('7 August 2022')

chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
chrome.find_element(By.ID, 'profession-1').click()


# By.LINK_TEXT

chrome.get('https://formy-project.herokuapp.com')
chrome.find_element(By.LINK_TEXT, 'Buttons').click()

chrome.get('https://the-internet.herokuapp.com/')
chrome.find_element(By.LINK_TEXT, 'Checkboxes').click()

chrome.get('https://the-internet.herokuapp.com/')
chrome.find_element(By.LINK_TEXT, 'Inputs').click()


# By.PARTIAL_LINK_TEXT

chrome.get('https://formy-project.herokuapp.com/')
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Key').click()

chrome.get('https://formy-project.herokuapp.com/')
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Switch').click()

chrome.get('https://the-internet.herokuapp.com/')
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Broken').click()


# By.Name

chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
chrome.find_element(By.NAME, 'firstname').send_keys('Cristiana')

chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
chrome.find_element(By.NAME, 'lastname').send_keys('Stan')

chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
chrome.find_element(By.NAME, 'continents').send_keys('Europe')


# By.TAG_NAME

chrome.get('https://formy-project.herokuapp.com/autocomplete')
chrome.find_element(By.TAG_NAME, 'input').send_keys('Bucuresti, Sector 3')

lista_input = chrome.find_elements(By.TAG_NAME, ' input')
lista_input[6].send_keys('Romania')

lista_input[5].send_keys('033064')


# By.CLASS_NAME

chrome.get('https://formy-project.herokuapp.com/autocomplete')
classname_list = chrome.find_elements(By.CLASS_NAME, 'form-control')

classname_list[0].send_keys('Bucuresti, Romania')

classname_list[5].send_keys('033064')

classname_list[6].send_keys('Romania')


sleep(5)
chrome.quit()


