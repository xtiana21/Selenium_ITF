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
chrome.get('http://www.seleniumframework.com/practiceform/')

#
chrome.find_element(By.NAME, 'country').send_keys('Romania')
chrome.find_element(By.NAME, 'company').send_keys('IT Factory')


sleep(5)
chrome.quit()