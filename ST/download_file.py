# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 01:57:25 2023

@author: Karan
"""

from selenium import webdriver
import time
from logindata import USERNAME,PASSWORD

# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
driver = webdriver.Firefox()
time.sleep(1)

driver.get('https://github.com/Karangupta-45/Spam_Detection-using-Deep-Learning-Techniques')
time.sleep(2)
code = driver.find_element_by_css_selector('#repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-main > div.file-navigation.mb-3.d-flex.flex-items-start > span.d-none.d-md-flex.ml-2 > get-repo > feature-callout')
code.click()
time.sleep(1)
download = driver.find_element_by_css_selector('#local-panel > ul > li:nth-child(3) > a')
download.click()
