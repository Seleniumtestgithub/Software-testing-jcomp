from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from logindata import USERNAME,PASSWORD
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import win32com.client as comclt
import logging

logging.basicConfig(filename="C:/Users/vidoo/OneDrive/Desktop/VIT/SEM_7/F1_ST/J_COMP/logs/app.log", format='%(filename)s %(asctime)s %(message)s', filemode='a')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
driver = webdriver.Firefox()
time.sleep(1)


driver.get('http://www.github.com')
time.sleep(3)

try:
    # Change: body -> ody
    continue_link = driver.find_element(By.CSS_SELECTOR, 'body > div.logged-out.env-production.page-responsive.header-overlay.home-campaign > div.position-relative.js-header-wrapper > header > div > div.HeaderMenu--logged-out.p-responsive.height-fit.position-lg-relative.d-lg-flex.flex-column.flex-auto.pt-7.pb-4.top-0 > div > div > div.position-relative.mr-lg-3.d-lg-inline-block > a')
    continue_link.click()
    time.sleep(3)
    if driver.find_element(By.NAME, 'login'):
        pass
    else:
        time.sleep(2)
        logger.error("Page not loaded...internet err")
    logger.info("Successfully loaded login page")
except Exception as e:
    logger.error(e)
    driver.quit()
    exit(1)

try:
    login = driver.find_element(By.NAME, 'login')
    password = driver.find_element(By.NAME, "password")

except Exception as e:
    logger.error(e)
    driver.quit()
    exit(1)

time.sleep(0.5)
    
login.send_keys(USERNAME)
logger.info("Entered username")
time.sleep(1)
    
password.send_keys(PASSWORD)
logger.info("Entered password")
time.sleep(1)

try:
    button = driver.find_element(By.NAME, 'commit')
    button.click()

except Exception as e:
    logger.error(e)
    driver.quit()
    exit(1)


