import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()


# exercitiu - upload fotografie

chrome.get('https://sendspace.com')   # deschidem pagina
input = chrome.find_element(By.ID, 'upload_file')  # cream variabila cu selector
input.send_keys("C:/Users/Cristiana/Pictures/crisss.jpg") # uploadam o poza

# exercitiu - completare username

chrome.get('https://www.sendspace.com/login.html')
time.sleep(3) # altfel da eroare deoarece comanda se executa inainte sa se incarce pagina

# user_input = chrome.find_element(By.ID, 'loginusername') # variabila cu selector by ID
user_input = chrome.find_element(By.CSS_SELECTOR, '#loginusername') # variabila cu CSS_SELECTOR by ID
user_input.send_keys('alabalaportocala') # input text

# exercitiu - click login button
chrome.get('https://www.sendspace.com/login.html')
login_button = chrome.find_element(By.CSS_SELECTOR, 'input[value="Log In"]') # selector format din atribut + valoare
login_button.click

chrome.get('https://www.sendspace.com/login.html')
login_button = chrome.find_element(By.CSS_SELECTOR, 'div>div>input') # selector construit din tata-fiu
login_button.click


# TIPURI - CSS_SELECTOR cu atribut

chrome.get("https://www.sendspace.com/login.html")
time.sleep(3)

# 1. tipul de element 'a' si in paranteza patrata atributul si valoarea
facebook_login_button = chrome.find_element(By.CSS_SELECTOR, 'a[title="log in with Facebook"]')

# 2.  tipul de element 'a' cu atributul 'title' care contine textul 'Facebook'
facebook_login_button = chrome.find_element(By.CSS_SELECTOR, 'a[title*="Facebook"]')

# 3. tipul de element 'a' cu atributul title care se termina cu textul Facebook
facebook_login_button = chrome.find_element(By.CSS_SELECTOR, 'a[title$="Facebook"]')

# 4. tipul de element 'a' cu atributul title care incepe cu textul Facebook
# facebook_login_button = chrome.find_element(By.CSS_SELECTOR, 'a[title^="Facebook"]')



chrome.get("https://www.sendspace.com/login.html")

# slector by ID
user = chrome.find_element(By.ID, "loginusername")

# selector By CSS - ID
user = chrome.find_element(By.CSS_SELECTOR, "#loginusername")

# selector by CLASS_NAME
user = chrome.find_element(By.CLASS_NAME, 'fa fa-facebook')

#selector CSS by CLASS
user = chrome.find_element(By.CSS_SELECTOR, '.fa.fa=facebook')

#selector CSS format din [atribut = valoare]
user = chrome.find_element(By.CSS_SELECTOR, '[class = fa fa-facebook]')



# XPATH_SELECTOR

user = chrome.find_element(By.XPATH, '//input[@id="loginusername"]')
user = chrome.find_element(By.XPATH, '//input[@name="username"]')


# orice tip de element care are atributul name = username

user = chrome.find_element(By.XPATH, '//*[@name="username"]')
user = chrome.find_element(By.CSS_SELECTOR, 'input[id="loginusername"]')

login_button = chrome.find_element(By.XPATH, '//div/div/input')
login_button = chrome.find_element(By.CSS_SELECTOR, 'input[value=''Log In'']')


sleep(5)
chrome.quit()