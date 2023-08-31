from selenium import webdriver
import time
from logindata import USERNAME,PASSWORD

# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
driver = webdriver.Firefox()
time.sleep(1)


driver.get('http://www.github.com')


driver.get('http://www.github.com')
new_repository = driver.find_element_by_link_text('New')
new_repository.click()
time.sleep(2)

repository_name = driver.find_element_by_id('repository_name')
repository_name.send_keys('github-automation-p89')
time.sleep(2)

repository_description = driver.find_element_by_id('repository_description')
repository_description.send_keys('GitHub Automation Using Selenium Part')
time.sleep(2)

repository_auto_init = driver.find_element_by_id('repository_auto_init')
repository_auto_init.click()
time.sleep(2)   

create_repo_button = driver.find_element_by_css_selector('button.btn')
create_repo_button.click()
time.sleep(2)   