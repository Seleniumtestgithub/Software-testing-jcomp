from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from logindata import USERNAME,PASSWORD
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import win32com.client as comclt


# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
driver = webdriver.Firefox()
time.sleep(1)


driver.get('http://www.github.com')
time.sleep(3)

continue_link = driver.find_element(By.CSS_SELECTOR, 'body > div.logged-out.env-production.page-responsive.header-overlay.home-campaign > div.position-relative.js-header-wrapper > header > div > div.HeaderMenu--logged-out.p-responsive.height-fit.position-lg-relative.d-lg-flex.flex-column.flex-auto.pt-7.pb-4.top-0 > div > div > div.position-relative.mr-lg-3.d-lg-inline-block > a')
continue_link.click()
time.sleep(3)
if driver.find_element(By.NAME, 'login'):
    pass
else:
    time.sleep(2)
    
login = driver.find_element(By.NAME, 'login')
password = driver.find_element(By.NAME, "password")
time.sleep(0.5)
    
login.send_keys(USERNAME)
time.sleep(1)
    
password.send_keys(PASSWORD)
time.sleep(1)
    
button = driver.find_element(By.NAME, 'commit')
button.click()
print ("Here 1")
time.sleep(5)
print ("Here 2")


#create repo 

new_repository = driver.find_element(By.ID, 'global-create-menu-button')
new_repository.click()
time.sleep(1)
new_repository2 = driver.find_element(By.LINK_TEXT, 'New repository')
new_repository2.click()
time.sleep(5)

repository_name = driver.find_element(By.ID, ':r2:')
repository_name.send_keys('github-automation-p9999')
time.sleep(2)

repository_description = driver.find_element(By.ID, ':r3:')
repository_description.send_keys('GitHub Automation Using Selenium Part')
time.sleep(2)

repository_auto_init = driver.find_element(By.ID, ':r8:')
repository_auto_init.click()
time.sleep(2)   

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

create_repo_button = driver.find_element(By.XPATH, '//button[@class="types__StyledButton-sc-ws60qy-0 iqZIXT"]')
create_repo_button.click()
time.sleep(5)

print("Here 3")

# Upload file

repo_link = driver.find_element(By.XPATH, '//summary[@class="btn ml-2"]')
repo_link.click()
time.sleep(4)
upload_button = driver.find_element(By.LINK_TEXT, 'Upload files')
#upload_button = driver.find_element_by_xpath('//*[@id="repo-content-pjax-container"]/div/div/div[2]/div[1]/div[2]/details/summary')
upload_button.click()
time.sleep(3)

print("Here 4")

upload_button2 = driver.find_element(By.XPATH, '//p[@class="repo-file-upload-choose"]')
upload_button2.click()

time.sleep(5)

wsh= comclt.Dispatch("WScript.Shell")
#wsh.AppActivate("Notepad") # select another application
wsh.SendKeys("{TAB}") # send the keys you want
time.sleep(1)
wsh.SendKeys("{TAB}")
time.sleep(1)
wsh.SendKeys("{TAB}")
time.sleep(1)
wsh.SendKeys("{TAB}")
time.sleep(1)
wsh.SendKeys("{TAB}")
time.sleep(1)
wsh.SendKeys("{TAB}")
time.sleep(1)
wsh.SendKeys("{TAB}")
time.sleep(1)
wsh.SendKeys("{TAB}")
time.sleep(1)
# wsh.SendKeys("{TAB}")
# time.sleep(1)
wsh.SendKeys("{DOWN}")
time.sleep(1)
wsh.SendKeys("{DOWN}")
time.sleep(1)   
wsh.SendKeys("{DOWN}")
time.sleep(1)
wsh.SendKeys("{DOWN}")
time.sleep(1)
wsh.SendKeys("{ENTER}")
time.sleep(1)
wsh.SendKeys("{TAB}")
time.sleep(1)
wsh.SendKeys("{DOWN}")
time.sleep(1)
wsh.SendKeys("{UP}")
time.sleep(1)
wsh.SendKeys("{ENTER}")
# actions = ActionChains(driver)
# actions.send_keys(Keys.TAB) #8
# actions.send_keys(Keys.TAB) #8
# actions.send_keys(Keys.TAB) #8
# actions.send_keys(Keys.TAB) #8
# actions.send_keys(Keys.TAB) #8
# actions.send_keys(Keys.TAB) #8
# actions.send_keys(Keys.TAB) #8
# actions.send_keys(Keys.TAB) #8
# actions.send_keys(Keys.DOWN) #4
# actions.send_keys(Keys.DOWN) #4
# actions.send_keys(Keys.DOWN) #4
# actions.send_keys(Keys.DOWN) #4
# actions.send_keys(Keys.ENTER) #1
# actions.send_keys(Keys.TAB) #1
# actions.send_keys(Keys.DOWN) #1
# actions.send_keys(Keys.UP) #1
# actions.send_keys(Keys.ENTER)

# actions.perform()

time.sleep(15)

commit_changes = driver.find_element(By.XPATH, '//button[@class="js-blob-submit btn-primary btn"]')
commit_changes.click()

time.sleep(15)


#upload_file = driver.find_element_by_css_selector("#repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-main > div.file-navigation.mb-3.d-flex.flex-items-start > details > div > ul > li:nth-child(4) > a")
#upload_file = driver.find_element_by_xpath('//*[@id="repo-content-turbo-frame"]/div/div/div[2]/div[1]/div[2]/details/div/ul/li[4]/a')
##upload_file.click()
#time.sleep(2)
#upload_file_cl = driver.find_element_by_css_selector("#upload-manifest-files-input")

# upload_file_cl = driver.find_element_by_xpath('/html/body/div[1]/div[6]/div/main/turbo-frame/div/div/div[2]/form[2]/file-attachment/p/input')
#upload_file_cl.click()
#time.sleep(1)
#upload_file_cl.send_keys(r'C:\Users\Karan\Desktop\soft_test_file\Right-wing-all-terms')
#time.sleep(5)

#commit_upload = driver.find_element_by_xpath('//*[@id="repo-content-pjax-container"]/div/form/button')
#commit_upload.click()

#repo_link = driver.find_element_by_css_selector('#user-profile-frame > div > div:nth-child(1) > div > ol > li:nth-child(1) > div > div > div > a')


# existing repo download file

driver.get('https://github.com/Vidoosh/Image-colorizer')
time.sleep(2)
code = driver.find_element(By.CSS_SELECTOR, '#repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-main > div.file-navigation.mb-3.d-flex.flex-items-start > span.d-none.d-md-flex.ml-2 > get-repo > feature-callout')
code.click()
time.sleep(1)
download = driver.find_element(By.CSS_SELECTOR, '#local-panel > ul > li:nth-child(3) > a')
download.click()


# edit profile

# profile = driver.find_element_by_css_selector('body > div.logged-in.env-production.page-responsive > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary')
# profile.click()
# time.sleep(2)

# your_profile = driver.find_element(By.CSS_SELECTOR, 'body > div.logged-in.env-production.page-responsive > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > a:nth-child(6)')
# your_profile.click()
# time.sleep(2)

# edit_profile = driver.find_element(By.CSS_SELECTOR, 'body > div.logged-in.env-production.page-responsive.page-profile.mine > div.application-main > main > div.container-xl.px-3.px-md-4.px-lg-5 > div > div.Layout-sidebar > div > div.js-profile-editable-replace > div.d-flex.flex-column > div.js-profile-editable-area.d-flex.flex-column.d-md-block > div:nth-child(2) > button')
# edit_profile.click()
# time.sleep(2)