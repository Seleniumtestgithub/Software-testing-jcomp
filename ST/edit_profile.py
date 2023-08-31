from selenium import webdriver
import time
from logindata import USERNAME,PASSWORD

# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
driver = webdriver.Firefox()
time.sleep(1)


driver.get('http://www.github.com')
time.sleep(1)

profile = driver.find_element_by_css_selector('body > div.logged-in.env-production.page-responsive > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary')
profile.click()
time.sleep(2)

your_profile = driver.find_element_by_css_selector('body > div.logged-in.env-production.page-responsive > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > a:nth-child(6)')
your_profile.click()
time.sleep(2)

edit_profile = driver.find_element_by_css_selector('body > div.logged-in.env-production.page-responsive.page-profile.mine > div.application-main > main > div.container-xl.px-3.px-md-4.px-lg-5 > div > div.Layout-sidebar > div > div.js-profile-editable-replace > div.d-flex.flex-column > div.js-profile-editable-area.d-flex.flex-column.d-md-block > div:nth-child(2) > button')
edit_profile.click()
time.sleep(2)