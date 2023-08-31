from selenium import webdriver
import time
import logindata

# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
driver = webdriver.Firefox()
time.sleep(2)

driver.get('http://www.github.com')
time.sleep(5)

continue_link = driver.find_element_by_link_text('Sign in')
continue_link.click()
time.sleep(5)
if driver.find_element_by_name('login'):
    pass
else:
    time.sleep(5)
    
login = driver.find_element_by_name('login')
password = driver.find_element_by_name("password")
time.sleep(0.5)
    
login.send_keys(logindata.USERNAME)
time.sleep(1)
    
password.send_keys(logindata.PASSWORD)
time.sleep(1)
    
button = driver.find_element_by_name('commit')
button.click()
time.sleep(5)
