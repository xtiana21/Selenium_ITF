from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#initializam un browser
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome.maximize_window()

# SLEEP
# opreste executia codului pt un anumit timp de secunde
# nu se recomanda sa se foloseasca in general

# IMPLICIT WAIT
# stabileste in tot proiectul/in tot testul, cate secunde sa caute selenium ca sa gaseasca un element pe pagina
chrome.implicitly_wait(3)

# EXPLICIT WAIT
# se recomanda sa se foloseasca doar in anumite cazuri, pe o anumita bucata de cod
chrome.get('https://www.sendspace.com/login.html')
login_button = WebDriverWait(chrome,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='Log In']")))
login_button.click()


chrome.quit()