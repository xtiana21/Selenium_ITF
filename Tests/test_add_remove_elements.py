import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



def test_check_add_element_functionality():
    s = Service(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=s)
    chrome.maximize_window()
    chrome.implicitly_wait(3)

    chrome.get('https://the-internet.herokuapp.com/add_remove_elements/')
    add_element_button = chrome.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]')
    add_element_button.click()
    add_element_button.send_keys()

    delete_button = chrome.find_element(By.CLASS_NAME, 'added-manually')
    assert delete_button.is_displayed()

    time.sleep(5)
    chrome.quit()

def test_check_url():
    pass

def test_title():
    pass

def test_link():
    pass

def test_add_and_delete_functionality():
    s = Service(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=s)
    chrome.maximize_window()
    chrome.implicitly_wait(3)
    chrome.get('https://the-internet.herokuapp.com/add_remove_elements/')

    add_element_button = chrome.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]')
    for i in range(10): # executam de mai multe ori o functie
        add_element_button.click()

    delete_button_list = chrome.find_elements(By.CLASS_NAME, 'added-manually')
    assert len(delete_button_list) == 10, 'Check all delete button is displayed'

    for i in range (10):
        delete_button_list.click()
        assert len(delete_button_list) == 10-i-1

    sleep(5)
    time.sleep(5)
    chrome.quit()


