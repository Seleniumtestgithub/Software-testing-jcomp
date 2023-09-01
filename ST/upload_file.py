from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from logindata import USERNAME,PASSWORD

# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
driver = webdriver.Firefox()
time.sleep(1)


driver.get('http://www.github.com')

repo_link = driver.find_element(By.XPATH, '/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/ul/li[1]/div/a/span[2]')
repo_link.click()
time.sleep(1)
time.sleep(2)
upload_button = driver.find_element(By.CSS_SELECTOR, "#repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-main > div.file-navigation.mb-3.d-flex.flex-items-start > details > summary")
upload_button = driver.find_element(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div/div[2]/div[1]/div[2]/details/summary')
upload_button.click()
time.sleep(2)

upload_file = driver.find_element(By.CSS_SELECTOR, "#repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-main > div.file-navigation.mb-3.d-flex.flex-items-start > details > div > ul > li:nth-child(4) > a")
upload_file = driver.find_element(By.XPATH, '//*[@id="repo-content-turbo-frame"]/div/div/div[2]/div[1]/div[2]/details/div/ul/li[4]/a')
upload_file.click()
time.sleep(2)
upload_file_cl = driver.find_element(By.CSS_SELECTOR, "#upload-manifest-files-input")