from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logindata

# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
driver = webdriver.Firefox()
time.sleep(2)

driver.get('http://www.github.com')
time.sleep(5)

continue_link = driver.find_element(By.LINK_TEXT, 'Sign in')
continue_link.click()
time.sleep(5)
if driver.find_element(By.NAME, 'login'):
    pass
else:
    time.sleep(5)

login = driver.find_element(By.NAME, 'login')
password = driver.find_element(By.NAME, 'password')
time.sleep(0.5)
    
login.send_keys(logindata.USERNAME)
time.sleep(1)
    
password.send_keys(logindata.PASSWORD)
time.sleep(1)
    
button = driver.find_element(By.NAME, 'commit')
button.click()
time.sleep(5)